# RTTM Viewer

<p align="center">
<img src="/demo.gif" title="Demo" />
</p>

Rich Transcription Time Marked (RTTM) is a data format typically used to represent speaker diarization annotations.
RTTM Viewer allows you to quickly visualize RTTM files in an interactive way thanks to [plotly](https://github.com/plotly/plotly.py).

## Install

**Note:** RTTM Viewer can only be installed as an application on Linux. Pull requests are welcome :)

```shell
git clone https://github.com/juanmc2005/rttm-viewer.git
cd rttm-viewer
pip install -r requirements.txt

python view_rttm.py /path/to/rttm/file

# If you're on Linux, install to open RTTM files with a right click
python install.py
```

## License

```
MIT License

Copyright (c) 2022 Juan Manuel Coria

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
