# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
###import Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# Loading the Image
# =============================================================================
org_img=cv2.imread('mdb168.pgm',0)
cv2.namedWindow("Lena in Gray", cv2.WINDOW_NORMAL)
cv2.imshow('Lena in Gray',org_img)
cv2.waitKey(0)


# =============================================================================
# Applying Guasssians plur
# =============================================================================
blur_img = cv2.GaussianBlur(org_img,(3,3),0)
cv2.namedWindow("blur in Gray", cv2.WINDOW_NORMAL)
cv2.imshow('blur in Gray',blur_img)
cv2.waitKey(0)
# =============================================================================
# Applying laplacian
# =============================================================================
laplacian = cv2.Laplacian(blur_img,cv2.CV_64F)
cv2.namedWindow("Laplacian", cv2.WINDOW_NORMAL)
cv2.imshow('Laplacian',laplacian)
cv2.waitKey(0)
# =============================================================================
# Applying sobel
# =============================================================================
sobelx = cv2.Sobel(blur_img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(blur_img,cv2.CV_64F,0,1)

cv2.namedWindow("Sobelx", cv2.WINDOW_NORMAL)
cv2.imshow('Sobelx',sobelx)
cv2.waitKey(0)
cv2.namedWindow("Sobely", cv2.WINDOW_NORMAL)
cv2.imshow('Sobely',sobely)
cv2.waitKey(0)

# The sobelX and sobelY images are now of the floating
# point data type -- we need to take care when converting
# back to an 8-bit unsigned integer that we do not miss
# any images due to clipping values outside the range
# of [0, 255]. First, we take the absolute value of the
# graident magnitude images, THEN we convert them back
# to 8-bit unsigned integers
sobelX = np.uint8(np.absolute(sobelx))
sobelY = np.uint8(np.absolute(sobely))

# We can combine our Sobel gradient images using our
# bitwise OR
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

# Show our Sobel images
cv2.namedWindow("Sobel X", cv2.WINDOW_NORMAL)
cv2.imshow("Sobel X", sobelX)
cv2.namedWindow("Sobel Y", cv2.WINDOW_NORMAL)
cv2.imshow("Sobel Y", sobelY)
cv2.namedWindow("Sobel Combined", cv2.WINDOW_NORMAL)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)

# =============================================================================
###CannyL2gradient
# =============================================================================
canny = cv2.Canny(blur_img, 30, 120)
cv2.namedWindow("Canny", cv2.WINDOW_NORMAL)
cv2.imshow("Canny", canny)
cv2.imwrite("canny-img.png", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

# =============================================================================
# for x in range(10, 60, 5):
      #for y in range(90, 210, 5):

        #canny = cv2.Canny(image, x, y)
        #cv2.putText(canny, "x:"+str(x)+" y:"+str(y), (500, 650), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
        #cv2.imwrite("_canny-img-"+str(x)+"-"+str(y)+".png", canny)
# =============================================================================
