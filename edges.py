import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt 
from PIL import Image, ImageOps

class Edges:
	def __init__(self, image):
		self.img = cv.imread(image)
		self.grey = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
		self.kernel = np.ones((2,2), np.uint8)

	def edges(self):
		edges = cv.Canny(self.grey, 200, 300)
		blr = cv.GaussianBlur(edges, (3,3), 0)
		image_grey = 255 - dil 
		image_rgba = cv.cvtColor(image_grey, cv.COLOR_BGR2GRAY)
		white = np.all(image_rgba == [255,255,255,255], axis = -1)
		image_rgba[white, -1] = 0
		cv.imwrite("edges.png", image_grey)
		return image_grey