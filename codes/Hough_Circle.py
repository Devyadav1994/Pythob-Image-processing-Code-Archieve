# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:41:01 2018

@author: Fakrul-IslamTUSHAR
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import reconstruction
import cv2.cv as cv


# =============================================================================
# Hough Circle
# =============================================================================
img = cv2.imread('ISIC_0000071.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()