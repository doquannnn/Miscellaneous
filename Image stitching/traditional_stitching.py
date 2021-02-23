import cv2
import imutils
import numpy as np
from panorama import Stitcher

img1 = cv2.imread('images/fansipan/right_fansipan.jpg')
img2 = cv2.imread('images/fansipan/left_fansipan.jpg')

stitcher = Stitcher()
result = stitcher.stitch(img1, img2)

cv2.imshow('stitched', result)
cv2.waitKey(0)
