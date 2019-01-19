# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:52:47 2018

@author: Fakrul-IslamTUSHAR
"""

# =============================================================================
# Feature Matching.
# =============================================================================
import cv2
import urllib
import numpy as np
import matplotlib.pyplot as plt


def showImage(img):
    plt.axis('off')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("messi.jpg")
showImage(img)
productImage = cv2.imread("messiface.jpg")
showImage(productImage)

flann = cv2.FlannBasedMatcher({'algorithm': 0, 'trees': 8}, {'checks': 100})
detector = cv2.SIFT()
kpts1, descs1 = detector.detectAndCompute(productImage, None)
kpts2, descs2 = detector.detectAndCompute(img, None)
matches = [m for (m, n) in flann.knnMatch(descs1, descs2, k=2) if m.distance < 0.8 * n.distance]
sourcePoints = np.float32([kpts1[m.queryIdx].pt for m in matches]).reshape(-1, 2)
destPoints = np.float32([kpts2[m.trainIdx].pt for m in matches]).reshape(-1, 2)
M, mask = cv2.findHomography(sourcePoints, destPoints, cv2.RANSAC, 11.0)

def drawMatches(img1, kpts1, img2, kpts2, matches):
    # combine both images
    out = np.zeros((max([img1.shape[0], img2.shape[0]]), img1.shape[1] + img2.shape[1], 3), dtype='uint8')
    out[: img1.shape[0], : img1.shape[1]] = img1
    out[: img2.shape[0], img1.shape[1]:] = img2
    # draw the lines
    for match in matches:
        (x1, y1) = kpts1[match.queryIdx].pt
        (x2, y2) = kpts2[match.trainIdx].pt
        cv2.line(out, (int(x1), int(y1)), (int(x2) + img1.shape[1], int(y2)), (0, 0, 255), 4)
    return out
showImage(drawMatches(productImage, kpts1, img, kpts2, np.array(matches)[[np.where(mask.ravel() == 1)[0]]]))

def drawRegions(source, res, regions, color=(0, 0, 255), size=4):
    for (x, y, w, h) in regions:
        res[y: y + h, x: x + w] = source[y: y + h, x: x + w]
        cv2.rectangle(res, (x, y), (x + w, y + h), color, size)
    return res

faded = (img * 0.65).astype(np.uint8)

pp = destPoints[mask.ravel() == 1]
xmin = pp[:, 0].min()
ymin = pp[:, 1].min()
productRegions = np.array([xmin, ymin, pp[:, 0].max() - xmin, pp[:, 1].max() - ymin]).astype(np.int32).reshape(1, 4)
showImage(drawRegions(img, faded.copy(), productRegions, (0, 255, 0)))