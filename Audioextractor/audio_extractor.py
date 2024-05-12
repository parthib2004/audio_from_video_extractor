# pip install moviepy

import moviepy.editor

cvt_video = moviepy.editor.VideoFileClip("#Here write the name of the video file")
ext_audio = cvt_video.audio
ext_audio.write_audiofile("extracted_audio.mp3")
