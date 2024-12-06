from moviepy.editor import *

# Load the video file
clip = VideoFileClip(r"C:\Users\Admin\Desktop\S Python\Moviepy\myvideo.mp4")

# Get video dimensions
width, height = clip.size
print("Video size:", width, height)

# Create a subclip (from 0 th to 2th second)
subclip = clip.subclip(0, 2)
subclip.write_videofile(r"C:\Users\Admin\Desktop\S Python\Moviepy\subclip.mp4")
