# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:54:25 2018

@author: Fakrul-IslamTUSHAR
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


# =============================================================================
# Loading the Image
# =============================================================================
img=cv2.imread('ISIC_0000043.jpg',-1)
cv2.namedWindow("messi", cv2.WINDOW_NORMAL)
cv2.imshow('messi',img)
cv2.waitKey(0)

# =============================================================================
# 
# =============================================================================
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
# =============================================================================
# =============================================================================

rect = (333,49,1500,1500)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,10,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()
cv2.namedWindow("messi2", cv2.WINDOW_NORMAL)
cv2.imshow('messi2',img)
cv2.waitKey(0)

cv2.destroyAllWindows()