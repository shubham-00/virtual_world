# pip uninstall pytube
# pip uninstall pytube3
# pip install pytube3

import pytube
from pytube.cli import on_progress

url = input("Enter video url: ")

yt = pytube.YouTube(url, on_progress_callback=on_progress)
# yt = yt.streams[0].download()
yt.streams.get_highest_resolution().download()

