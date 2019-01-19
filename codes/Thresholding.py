# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 19:34:57 2018

@author: Fakrul-IslamTUSHAR
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('ISIC_0000043.jpg',0)
img = cv.medianBlur(img,5)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,125,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)

blur = cv.GaussianBlur(th3,(5,5),0)
ret3,th4 = cv.threshold(blur,0,125,cv.THRESH_BINARY+cv.THRESH_OTSU)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


sub=cv.bitwise_and(img, img, mask=th4)

cv2.namedWindow("Guassians", cv2.WINDOW_NORMAL)
cv.imshow('Guassians',th3)
cv2.namedWindow("otsu", cv2.WINDOW_NORMAL)
cv.imshow('otsu',th4)
cv2.namedWindow("sub", cv2.WINDOW_NORMAL)
cv.imshow('sub',sub)
cv.waitKey(0)
cv.destroyAllWindows()
