from moviepy.editor import *

# Load the video file
clip = VideoFileClip(r"C:\Users\Admin\Desktop\S Python\Moviepy\myvideo.mp4")

# Rotate the video by 45 degrees
rotated_clip = clip.rotate(45)
rotated_clip.write_videofile(r"C:\Users\Admin\Desktop\S Python\Moviepy\rotated_video.mp4")

# Increase audio volume by 50%
louder_clip = clip.volumex(1.5)
louder_clip.write_videofile(r"C:\Users\Admin\Desktop\S Python\Moviepy\louder_video.mp4")
