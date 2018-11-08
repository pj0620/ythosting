from transformations import *

def process(transformation):
	transformation.transform()
	transformation.invert()
	
process(Flip())