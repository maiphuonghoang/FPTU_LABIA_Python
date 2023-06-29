
"""
from pytube import YouTube

link = input("Enter Link: ")
yt = YouTube(link)
vid = yt.streams.get_highest_resolution()
vid.download()
print("Done")
"""
from pytube import YouTube
import urllib.error


link = input("Enter Link: ")

try:
    yt = YouTube(link)
    vid = yt.streams.get_highest_resolution()
    vid.download()
    print("Done")
except urllib.error.HTTPError as e:
    if e.code == 410:
        print("The video is no longer available.")
    else:
        print("An error occurred:", e)
