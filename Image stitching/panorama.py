import numpy as np
import cv2
import imutils


class Stitcher:
    def __init__(self, ratio=0.75, reprojThresh=5.0, final_image=True, rotated=False):
        self.ratio = ratio
        self.reprojThresh = reprojThresh
        self.final_image = final_image
        self.rotated = rotated

    def stitch(self, imageA, imageB):
        (kptsA, descA) = self.detectAndDescribe(imageA)
        (kptsB, descB) = self.detectAndDescribe(imageB)

        M = self.matchKeypoints(descA, descB, kptsA, kptsB)

        if M is None:
            return None

        H = M
        if self.rotated:
            stitched_image = cv2.warpPerspective(imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]
                                                             + imageB.shape[0]))
        else:
            stitched_image = cv2.warpPerspective(
                imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))

        if self.final_image:
            stitched_image[0:imageB.shape[0], 0:imageB.shape[1]] = imageB

        return stitched_image

    def detectAndDescribe(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sift = cv2.SIFT_create()
        (kpts, descs) = sift.detectAndCompute(gray, None)

        return [keypoint.pt for keypoint in kpts], descs

    def matchKeypoints(self, descA, descB, kptsA, kptsB):
        matcher = cv2.BFMatcher()
        matches = matcher.knnMatch(descA, descB, k=2)

        good = []
        for first, second in matches:
            if first.distance < self.ratio * second.distance:
                good.append((first.queryIdx, first.trainIdx))

        if len(good) > 4:
            ptsA, ptsB = [], []

            for src, desc in good:
                ptsA.append(kptsA[src])
                ptsB.append(kptsB[desc])

            H, _ = cv2.findHomography(np.float32(ptsA), np.float32(
                ptsB), cv2.RANSAC, self.reprojThresh)

            return H

        return None
