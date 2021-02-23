import numpy as np
import cv2
from imutils import paths
import imutils

imagePaths = sorted(paths.list_images('images/countryside'))

images = [cv2.imread(imagePath) for imagePath in imagePaths]

stitcher = cv2.Stitcher_create()
(status, original_stitched) = stitcher.stitch(images)

if status != 0:
    if status == 1:
        if len(images) > 2:
            print('More images!')
        else:
            print('More images or rerun again due to probablistic model')
    if status == 2:
        print('RANSAC failed to estimate homography matrix, lack of keypoints for matching, \
            more images!')
    elif status == 3:
        print('Not discover yet, do it yourself ^^')
    exit()


def better_stitched(original_stitched):
    stitched = cv2.copyMakeBorder(
        original_stitched, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
    gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

    contours, _ = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key=cv2.contourArea)
    (x, y, w, h) = cv2.boundingRect(c)

    mask = np.zeros(thresh.shape, dtype='uint8')
    cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

    minRect = mask.copy()
    sub = np.ones_like(mask, dtype='uint8')

    while cv2.countNonZero(sub) > 0:
        minRect = cv2.erode(minRect, None)
        sub = cv2.subtract(minRect, thresh)

    cnts = cv2.findContours(
        minRect.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    (x, y, w, h) = cv2.boundingRect(c)

    return stitched[y:y + h, x:x + w]


stitched = better_stitched(original_stitched)

for id, image in enumerate(images):
    cv2.imshow(f'image + {id}', image)

cv2.waitKey()

# cv2.imshow('primitive stitching', original_stitched)
# cv2.imshow('better stitching', stitched)
# cv2.waitKey()
