# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 05:57:00 2018

@author: Fakrul-IslamTUSHAR
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import reconstruction


def regional_filter(z, h):
    """Perform a h-dome regional filtering of the an image for background
    subtraction.

    Parameters
    ----------
    h : float
        h-dome cutoff value.

    Returns
    -------
        h-dome subtracted image as np.array
    """
    seed = np.copy(z)
    seed = z - h
    mask = z
    dilated = reconstruction(seed, mask, method='dilation')

    return z - dilated

 
org_img = cv2.imread("galaxy.jpg",0)
cv2.namedWindow("galaxy", cv2.WINDOW_NORMAL)
cv2.imshow('galaxy',org_img)
cv2.waitKey(0)

re= regional_filter(org_img,0.8)
cv2.namedWindow("re", cv2.WINDOW_NORMAL)
cv2.imshow('re',re)
cv2.waitKey(0)

cv2.namedWindow("Org-Re", cv2.WINDOW_NORMAL)
cv2.imshow('Org-Re',org_img-re)
cv2.waitKey(0)
cv2.destroyAllWindows()