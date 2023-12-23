from pytube import YouTube

import tkinter as tk
from tkinter import filedialog

def yt_mp3(url, save_path):
  """Filter through yt video and select only audio file"""
  try:
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(output_path=save_path)
    print("mp3 downloaded successfully!")
    
  except Exception as error:
    print(error)
    
