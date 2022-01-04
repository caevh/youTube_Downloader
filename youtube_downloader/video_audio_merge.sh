#!/bin/bash

video_title=$1
echo $video_title

ffmpeg -i ../output/video/$video_title -i ../output/audio/$video_title -c copy ../output/combined_audio_video/output_$video_title
