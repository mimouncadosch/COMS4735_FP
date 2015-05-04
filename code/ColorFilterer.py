import cv2 as cv
import numpy as np
from HoughLines import *

class ColorFilterer(object):
    """docstring for ColorFilterer"""
    def __init__(self):
        super(ColorFilterer, self).__init__()
        # self.arg = arg

    def filter_by_color(self, img):
        """
        Filter image by color for the colors of the lane markings
        """
        # Filter image by color
        # Color ranges
        # OpenCV is BGR
        white_lb = (180, 170, 170)
        white_ub = (255, 255, 255)
        yellow_lb = (0, 150, 140)
        yellow_ub = (150, 255, 255)

        # Masks for color filtering
        color_mask_white = cv.inRange(img, white_lb, white_ub)
        color_mask_yellow = cv.inRange(img, yellow_lb, yellow_ub)

        white_filtered_img = cv.bitwise_and(img, img, mask = color_mask_white)
        yellow_filtered_img = cv.bitwise_and(img, img, mask = color_mask_yellow)

        # 1) Erode yellow to get rid of green
        kernel = np.ones((5,5),np.uint8)
        yellow_filtered_img = cv.erode(yellow_filtered_img, kernel, iterations=1)

        # 2) Apply linear filter to yellow image to get rid of sky
        kernel_two = np.array([-1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1])
        # kernel = np.array([-1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1])
        # kernel = np.array([-1, 0, 1])
        white_filtered_img = cv.filter2D(white_filtered_img, cv.CV_8U, kernel_two)

        # 3) Combine image
        img = cv.bitwise_or(white_filtered_img, yellow_filtered_img, mask=None)

        # 4) Sobel operator get edges
        img = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=1)

        return img