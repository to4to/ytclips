import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

import subprocess
import json
from typing import List


#load Env Variables

from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

#load Api Key

youtube_url="https://www.youtube.com/watch?v=2TJxpyO3ei4"



#download the video

os.makedirs("downloaded_videos",exist_ok=True)

yt=YouTube(youtube_url)

video= yt.streams.filter(file_extension="mp4").first()

safe_title=yt.title.replace(' ','_')
filename=f'downloaded_videos/{safe_title}.mp4'

video.download(filename=filename)






