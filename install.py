from pathlib import Path
import shutil

installation_path = Path("~/.local/share/applications").expanduser()
script_path = installation_path / "RTTMViewer"
desktop_filename = "RTTMViewer.desktop"
script_filename = "view_rttm.py"

script_path.mkdir(parents=False, exist_ok=True)
shutil.copy(script_filename, str(script_path / script_filename))

with open(desktop_filename, "r") as file:
    text = file.read().format(path=str(script_path / script_filename))

with open(installation_path / desktop_filename, "w") as file:
    file.write(text)
