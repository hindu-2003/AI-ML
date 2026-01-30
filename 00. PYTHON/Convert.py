#Convert.py
#pip install moviepy
from moviepy.editor import *

# Load the video file
video = VideoFileClip("input_video.mp4")

# Extract the audio
audio = video.audio

# Save the audio as an MP3 file
audio.write_audiofile("output_audio.mp3")

# Close the audio and video clips to release resources
audio.close()
video.close()