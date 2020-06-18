import cv2 as cv
import numpy as np 
import random 
from edges import Edges 
from background import Background 
from PIL import Image, ImageOps

filename = "test.jpg"

class Draw:
	def __init__(self, image):
		self.img = cv.imread(image)
	
	def draw(self):
		grey = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
		inv = 255 - grey
		blur = cv.GaussianBlur(inv, (13,13),0)
		return cv.divide(grey, 255-blur, scale=255)

img = Image.open(filename)
draw = Draw(filename).draw()
cv.imwrite("draw.png", draw)
bg = Background(img.size, octaves=6).background()
edges = Edges(filename).edges
mask = edges[3]
draw = cv.bitwise_and(draw, edges, edges)
(thresh, draw) = cv.threshold(draw, 240, 255, cv.THRESH_BINARY)
h, w = draw.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
drawColor = cv.cvtColor(draw, cv.COLOR_BGR2GRAY)
cv.imwrite("final.png", drawColor)

final = Image.fromarray(drawColor)
final.show()