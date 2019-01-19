# -*- coding: utf-8 -*-
"""
Created on Wed May 16 13:14:41 2018

@author: Fakrul-IslamTUSHAR
"""
import cv2
import matplotlib.pyplot as plt

def showimg(img):
    plt.axis('off')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

org_img=cv2.imread("messi.jpg",-1)
showimg(org_img)
    
