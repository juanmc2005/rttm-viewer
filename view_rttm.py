import argparse
from typing import Dict, List

import plotly.graph_objs as go
from pyannote.core import Annotation
from pyannote.database.util import load_rttm


def as_dict_list(annotation: Annotation) -> Dict[str, List[Dict]]:
    result = {label: [] for label in annotation.labels()}
    for segment, track, label in annotation.itertracks(yield_label=True):
        result[label].append({
            "speaker": label,
            "start": segment.start,
            "end": segment.end,
            "duration": segment.duration,
            "track": track,
        })
    return result


def plot_annotation(annotation: Annotation):
    data = as_dict_list(annotation)
    fig = go.Figure(
        layout={
            'barmode': 'stack',
            'xaxis': {'automargin': True},
            'yaxis': {'automargin': True}
        }
    )
    for label, turns in data.items():
        durations, starts, ends = [], [], []
        for turn in turns:
            durations.append(turn["duration"])
            starts.append(turn["start"])
            ends.append(f"{turn['end']:.1f}")
        fig.add_bar(
            x=durations,
            y=[label] * len(durations),
            base=starts,
            orientation='h',
            showlegend=True,
            name=label,
            hovertemplate="<b>%{base:.2f} --> %{x:.2f}</b>",
        )

    fig.update_layout(
        title=annotation.uri,
        legend_title="Speakers",
        font={"size": 18},
        height=500,
        yaxis=go.layout.YAxis(showticklabels=False, showgrid=False),
        xaxis=go.layout.XAxis(title="Time (seconds)", showgrid=False),
    )
    fig.update_xaxes(rangemode="tozero")
    fig.update_traces(width=0.4)

    fig.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="RTTM file path")
    args = parser.parse_args()
    rttm = load_rttm(args.file)
    for uri, annotation in rttm.items():
        plot_annotation(annotation)
