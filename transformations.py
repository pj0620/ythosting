from moviepy.editor import *

#super class of all transformations
class Transformation:
	def transform(self,path):
		pass
	def invert(self,path):
		pass

#flips video		
class Flip(Transformation):
	def transform(self):
		encoded_video = VideoFileClip("input_video.mp4").rotate(180)
		encoded_video.write_videofile("encoded_video.mp4",fps=25)

	def invert(self):
		decoded_video = VideoFileClip("encoded_video.mp4").rotate(180)
		decoded_video.write_videofile("decoded_video.mp4",fps=25)