from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {}
os.chdir('C:/Users/God/Desktop/python wrkshop/google_videos')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])