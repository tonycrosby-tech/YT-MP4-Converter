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
    
def open_save_path():
  """Opens file dialog to select folder to save"""
  save_folder = filedialog.askdirectory()
  if save_folder:
    print(f"Selected folder: {save_folder}")
    
    return save_folder

if __name__ == "__main__":
  root = tk.Tk()
  root.withdraw()
  
  yt_url = input("Please enter a YT url: ")
  conv_dir = open_save_path()
  
  if conv_dir:
    print("Downloading mp3... Please wait.")
    yt_mp3(yt_url, conv_dir)
  else:
    print("Invalid save location.")