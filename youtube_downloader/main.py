from pytube import YouTube
import subprocess
import os
import pdb

url = input("URL: ").strip()
video_or_audio = input("Do you want video or audio or both?").strip()
if video_or_audio != "audio":
    resolution = input("Which resolution would you like? ").strip()
try:
    yt = YouTube(url)
except:
    print("URL is incorrect.")


def video_audio_streams(yt, video_or_audio, resolution=""):
    directory = os.getcwd()
    directory = directory[:-19]
    video_title, mp4_or_webm = video_filtering(resolution, yt)

    if video_or_audio == "both":
        video_streams = (
            yt.streams.filter(adaptive=True, res=resolution)
            .first()
            .download(directory + "/output/video/")
        )
        audio_streams = (
            yt.streams.filter(only_audio=True, mime_type=mp4_or_webm)
            .first()
            .download(directory + "/output/audio/")
        )

        print(video_streams)
        print(audio_streams)
        return video_streams, audio_streams, video_title, resolution

    elif video_or_audio == "audio":
        audio_streams = (
            yt.streams.filter(only_audio=True, mime_type=mp4_or_webm)
            .first()
            .download(directory + "/output/audio/")
        )

        return audio_streams, video_title

    else:
        video_streams = (
            yt.streams.filter(adaptive=True, res=resolution)
            .first()
            .download(directory + "/output/video/")
        )
        print(video_streams)
        return video_streams, video_title, resolution


def video_filtering(resolution, yt):
    if resolution == "2160p" or resolution == "1440p":
        video_title = yt.title + ".webm"
        video_title = video_title.translate({ord(i): None for i in "|"})
        mp4_or_webm = "audio/webm"
    else:
        video_title = yt.title + ".mp4"
        video_title = video_title.translate({ord(i): None for i in "|"})
        mp4_or_webm = "audio/mp4"

    return video_title, mp4_or_webm


if video_or_audio == "both":
    video_streams, audio_streams, video_title, resolution = video_audio_streams(
        yt, video_or_audio, resolution
    )
elif video_or_audio == "audio":
    audio_streams, video_title = video_audio_streams(yt, video_or_audio)
else:
    video_streams, video_title, resolution = video_audio_streams(
        yt, video_or_audio, resolution
    )


def file_renaming(video_title, video_or_audio, resolution=""):
    directory = os.getcwd()
    directory = directory[:-19]
    if resolution in ["2160p", "1440p"]:
        truncated_name = video_title[:4].replace(" ", "") + ".webm"
    else:
        truncated_name = video_title[:4].replace(" ", "") + ".mp4"
    if video_or_audio == "both":
        print(f"DIRECTORY:{directory[:-18]}")
        os.rename(
            f"{directory}/output/audio/{video_title}",
            f"{directory}/output/audio/" + truncated_name,
        )
        os.rename(
            f"{directory}/output/video/{video_title}",
            f"{directory}/output/video/" + truncated_name,
        )
    elif video_or_audio == "audio":
        os.rename(
            f"{directory}/output/audio/{video_title}",
            f"{directory}/output/audio/" + truncated_name,
        )
    else:
        os.rename(
            f"{directory}/output/video/{video_title}",
            f"{directory}/output/video/" + truncated_name,
        )

    return truncated_name


if video_or_audio != "audio":
    truncated_name = file_renaming(video_title, video_or_audio, resolution)
else:
    truncated_name = file_renaming(video_title, video_or_audio)


def merge_audio_and_video_streams(truncated_name):
    directory = os.getcwd()
    print(directory)
    subprocess.call([f"{directory}/video_audio_merge.sh", truncated_name])


if video_or_audio == "both":
    merge_audio_and_video_streams(truncated_name)
