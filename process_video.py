from transformations import *
import sys
from argparse import ArgumentParser

def process(path,transformation):
	transformation.transform(path)
	
if __name__ == "__main__":
	#setup argument parser
	parser = ArgumentParser()	
	parser.add_argument("-e", "--encode", dest="filename",
                    help="encodes video and saves it as encoded video", metavar="FILE")
		
	#parse input argument
	args = parser.parse_args()
	
	if (not (args.filename is None)):
		process(args.filename,Split(2))