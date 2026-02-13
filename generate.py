import sys
import requests
import urllib3
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

video_url = sys.argv[1]

base_path = "C:/Users/lenovo/.n8n-files/"
video_path = base_path + "video.mp4"
audio_path = base_path + "audio.mp3"
final_path = base_path + "final_video.mp4"

# Download video
video_response = requests.get(video_url, verify=False)
with open(video_path, "wb") as f:
    f.write(video_response.content)

video = VideoFileClip(video_path)
audio = AudioFileClip(audio_path)

# Extend video to match audio
clips = []
total_duration = 0

while total_duration < audio.duration:
    clips.append(video)
    total_duration += video.duration

extended_video = concatenate_videoclips(clips)
extended_video = extended_video.subclipped(0, audio.duration)

final = extended_video.with_audio(audio)

final.write_videofile(final_path, codec="libx264", audio_codec="aac")

print("DONE")
