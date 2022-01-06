from pytube import YouTube
from pprint import pprint
import subprocess
import os
import pdb

yt = YouTube('https://www.youtube.com/watch?v=hmm6O25BOSg')
video_title = yt.title + '.mp4'
print(video_title)

def video_audio_streams(yt):
    video_streams = yt.streams.filter(adaptive=True)
    audio_streams = yt.streams.filter(only_audio=True)
    return video_streams, audio_streams

video_streams, audio_streams = video_audio_streams(yt)

def video_audio_list(video_streams, audio_streams):
# Used to make the list of strings look nicer
    list_of_video_stream = [stream for stream in video_streams]
    list_of_audio_stream = [stream for stream in audio_streams]
    return list_of_video_stream, list_of_audio_stream

video_lst, audio_lst = video_audio_list(video_streams, audio_streams)

# print(video_lst)
# def video_download(video_lst, audio_lst):
#     video = video_lst[0]
#     audio = video_lst[-1]
#     #video.download('../output/video')
#     audio.download('../output/audio')

#video_download(video_lst, audio_lst)
# #pdb.set_trace()
# def file_renaming():
#     global video_title
#     video_title = video_title.translate({ord(i): None for i in '|'})
#     truncated_name = video_title[:4].replace(' ', '') + ".mp4"
#     os.rename(f'../output/audio/{video_title}', f'../output/audio/' + truncated_name)
#     os.rename(f'../output/video/{video_title}', f'../output/video/' + truncated_name)
#     return truncated_name

# truncated_name = file_renaming()

# def merge_audio_and_video_streams(truncated_name):    
#     subprocess.call(['/home/harry/Projects/youTube_downloader/youtube_downloader/video_audio_merge.sh', truncated_name])

# merge_audio_and_video_streams(truncated_name)
