# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 02:51:35 2018

@author: Fakrul-IslamTUSHAR
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import reconstruction

# =============================================================================
# Load Original Image
# =============================================================================
org_img = cv2.imread("ISIC_0000001_median_hsv.png",-1)
cv2.namedWindow("fingerprint.jpg", cv2.WINDOW_NORMAL)
cv2.imshow('fingerprint.jpg',org_img)
cv2.waitKey(0)

kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# =============================================================================
# Applying Opening
# =============================================================================
opening = cv2.morphologyEx(org_img, cv2.MORPH_OPEN, kernel)
cv2.namedWindow("Opening", cv2.WINDOW_NORMAL)
cv2.imshow('Opening',opening)
cv2.waitKey(0)
# =============================================================================
# Applying Closing
# =============================================================================
closing= cv2.morphologyEx(org_img, cv2.MORPH_CLOSE, kernel)
cv2.namedWindow("Closing", cv2.WINDOW_NORMAL)
cv2.imshow('Closing',closing)
cv2.waitKey(0)
# =============================================================================
# Morphological Gradient
# =============================================================================
gradient = cv2.morphologyEx(org_img, cv2.MORPH_GRADIENT, kernel)
cv2.namedWindow("gradient", cv2.WINDOW_NORMAL)
cv2.imshow('gradient',gradient)
cv2.waitKey(0)
# =============================================================================
# Top Hat = Input_Image- Opening
# =============================================================================
tophat = cv2.morphologyEx(org_img, cv2.MORPH_TOPHAT, kernel)
cv2.namedWindow("tophat", cv2.WINDOW_NORMAL)
cv2.imshow('tophat',tophat)
cv2.waitKey(0)

# =============================================================================
# BlackHat
# =============================================================================
blackhat = cv2.morphologyEx(org_img, cv2.MORPH_BLACKHAT, kernel)
cv2.namedWindow("blackhat", cv2.WINDOW_NORMAL)
cv2.imshow('blackhat',blackhat)
cv2.waitKey(0)
cv2.imwrite('blackhat.png',blackhat)
cv2.destroyAllWindows()


# =============================================================================
# morphological Reconstruction
# =============================================================================


#re=reconstruction(org_img, org_img, method='dilation', selem=None, offset=None)
#cv2.namedWindow("Reconstruction", cv2.WINDOW_NORMAL)
#cv2.imshow('Reconstruction',re)
#cv2.waitKey(0)
#
#cv2.namedWindow("Org-Re", cv2.WINDOW_NORMAL)
#cv2.imshow('Org-Re',re)
#cv2.waitKey(0)
###cv2.destroyAllWindows()
#
## =============================================================================
## interpolation
## =============================================================================
#res = cv2.resize(closing,None,fx=3, fy=3, interpolation = cv2.INTER_CUBIC)
#cv2.namedWindow("Res", cv2.WINDOW_NORMAL)
#cv2.imshow('Res',res)
#cv2.waitKey(0)
#cv2.destroyAllWindows()