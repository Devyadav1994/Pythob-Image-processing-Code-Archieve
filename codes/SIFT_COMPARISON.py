# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:53:21 2018

@author: Fakrul-IslamTUSHAR
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img1 = cv.imread('20587902_8dbbd4e51f549ff0_MG_R_CC_ANON_2.tif',0)          # queryImage
img2 = cv.imread('20587902_8dbbd4e51f549ff0_MG_R_CC_ANON.tif',0) # trainImage
# Initiate SIFT detector
sift = cv.SIFT()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,flags=2)
plt.imshow(img3),plt.show()