# from pytube import YouTube
# import tkinter as tk
# from tkinter import filedialog

# def download_video(url, save_path):
#     try:
#         yt = YouTube(url)
#         streams = yt.streams.filter(progressive = True, file_extension="mp4")
#         highest_res_stream = streams.get_highest_resolution()
#         highest_res_stream.download(output_path = save_path)
#         print("Video Downloaded Successfully")
#     except Exception as e:
#         print(e)

# url = "https://youtu.be/gZM4-g_N-VA?si=YqErTqYBGrtP4oJ9"
# save_path =r"E:\Coding Stuff\python"

# download_video(url, save_path)

from yt_dlp import YoutubeDL

url = "https://youtu.be/gZM4-g_N-VA"

save_path = r"E:\Coding Stuff\python\%(title)s.%(ext)s"

ydl_opts = {
    'outtmpl': save_path,
    'format': 'best'
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download Complete")