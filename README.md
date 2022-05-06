# RTTM Viewer

<p align="center">
<img src="/demo.gif" title="Demo" />
</p>

Rich Transcription Time Marked (RTTM) is a data format typically used to represent speaker diarization annotations.
RTTM Viewer allows you to quickly visualize RTTM files in an interactive way thanks to [plotly](https://github.com/plotly/plotly.py).

## Install

**Note:** RTTM Viewer can only be installed as an application on Linux. Pull requests are welcome :)

```commandline
git clone git@github.com:juanmc2005/rttm-viewer.git
cd rttm-viewer
pip install -r requirements.txt

python view_rttm.py /path/to/rttm/file

# If you're on Linux, install to open RTTM files with a right click
python install.py
```
