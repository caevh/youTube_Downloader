from typing import final
from pytube import YouTube
from pprint import pprint
import subprocess
import os
import pdb

url = input('URL: ').strip()
video_or_audio = input('Do you want video or audio or both?')
if video_or_audio != 'audio':
    resolution = input('Which resolution would you like? ').strip()
try:
    yt = YouTube(url)
except:
    print('URL is incorrect.')

def video_audio_streams(yt, resolution, video_or_audio):
    video_title, mp4_or_webm = video_filtering(resolution, yt)   
    
    if video_or_audio == 'both':
        video_streams = yt.streams.filter(adaptive=True, res=resolution).first().download('../output/video/')
        audio_streams = yt.streams.filter(only_audio=True, mime_type=mp4_or_webm).first().download('../output/audio/')
        
        return video_streams, audio_streams, video_title, resolution

    elif video_or_audio == 'audio':
        audio_streams = yt.streams.filter(only_audio=True, mime_type=mp4_or_webm).first().download('../output/audio/')
        
        return audio_streams, video_title, resolution

    else:
        video_streams = yt.streams.filter(adaptive=True, res=resolution).first().download('../output/video/')
        
        return video_streams, video_title, resolution

def video_filtering(resolution, yt):
    if resolution == '2160p' or resolution == '1440p':
        video_title = yt.title + '.webm'
        video_title = video_title.translate({ord(i): None for i in '|'})
        mp4_or_webm = 'audio/webm'
    else:
        video_title = yt.title + '.mp4'
        video_title = video_title.translate({ord(i): None for i in '|'})
        mp4_or_webm = 'audio/mp4'
    
    return video_title, mp4_or_webm

if video_or_audio == 'both':
    video_streams, audio_streams, video_title, resolution = video_audio_streams(yt, resolution, video_or_audio)
elif video_or_audio == 'audio':
    audio_streams, video_title, resolution = video_audio_streams(yt, resolution, video_or_audio)
else:
    video_streams, video_title, resolution = video_audio_streams(yt, resolution, video_or_audio)

def file_renaming(video_title, resolution, video_or_audio):
    if resolution in ['2160p', '1440p']:
        truncated_name = video_title[:4].replace(' ', '') + ".webm"
    else:
        truncated_name = video_title[:4].replace(' ', '') + ".mp4"
    if video_or_audio == 'both':
        os.rename(f'../output/audio/{video_title}', f'../output/audio/' + truncated_name)
        os.rename(f'../output/video/{video_title}', f'../output/video/' + truncated_name)
    elif video_or_audio == 'audio':
        os.rename(f'../output/audio/{video_title}', f'../output/audio/' + truncated_name)
    else:
        os.rename(f'../output/video/{video_title}', f'../output/video/' + truncated_name)

    return truncated_name

truncated_name = file_renaming(video_title, resolution, video_or_audio)

def merge_audio_and_video_streams(truncated_name):    
    subprocess.call(['/home/harry/Projects/youTube_downloader/youtube_downloader/video_audio_merge.sh', truncated_name])

if video_or_audio == 'both':
    merge_audio_and_video_streams(truncated_name)
