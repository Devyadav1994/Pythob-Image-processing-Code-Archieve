# -*- coding: utf-8 -*-
"""
Created on Fri May 25 03:03:32 2018

@author: Fakrul-IslamTUSHAR
"""
import cv2
import skimage 
import numpy as np
from matplotlib import pyplot as plt
from glob import glob
import os

img = cv2.imread('ISIC_0000001_AHE.png',-1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    
lower_green = np.array([50,100,100])
upper_green = np.array([100,255,255])
mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(img,img, mask= mask)
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.namedWindow("Res", cv2.WINDOW_NORMAL)
cv2.imshow("Res",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
