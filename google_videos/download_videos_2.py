# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:22:07 2019

@author: Dawar
"""

from pytube import YouTube
import os

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

downloadYouTube('https://www.youtube.com/watch?v=zNyYDHCg06c', 'C:\\Users\\God\\Desktop\\python wrkshop\\google_videos')