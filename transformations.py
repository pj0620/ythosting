from moviepy.editor import *
import moviepy.video.fx.all as vfx
import cv2

#super class of all transformations
class Transformation:
	def transform(self,path):
		pass
	def invert(self,path):
		pass
		
	#find width and height
	def find_width(self,path):
		vid = cv2.VideoCapture(path)
		return vid.get(cv2.CAP_PROP_FRAME_WIDTH)
	def find_height(self,path):
		vid = cv2.VideoCapture(path)
		return vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
		
#splits video in half
class Split(Transformation):
	def __init__(self,N):
		self.N  = N

	def transform(self,path):
		#load input clip
		input_clip = VideoFileClip(path)

		#find size of video
		width = self.find_width(path)
		height = self.find_height(path)

		#find height of each box
		dx = width/2.0
		dy = height/2.0
		
		#stores sub-videos
		sub_videos = []
		
		#loop over indices
		for i in range(self.N):
			for j in range(self.N):
			
				#cut up video
				sub_videos.append(input_clip.fx(vfx.crop,x1=i*dx,x2=(i+1)*dx,y1=j*dy, y2=(j+1)*dy))
		
		#loop over subvideos
		for i,sub_video in enumerate(sub_videos):
			sub_video.write_videofile(str(i) + ".mp4",fps=25)

	def invert(self,path):
		pass