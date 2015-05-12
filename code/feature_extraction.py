import cv2 as cv
import numpy as np
from ColorFilterer import *
from Filter import *

def extract_features(img, hl, vp):

    # 0) Setup
    y_max, x_max, depth = img.shape
    bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img, lines = hl.get_hough_lines(bw)


    filter = Filter()
    if lines is not None:
        filter.filter_lines(img, lines)


    # cv.imshow("bw a/f sobel", bw)
    # cv.waitKey(0)
    # k = np.array([-100, -100, -100, -100, 0, 100, 100, 100, 40])
    # k = np.array([40, 40, 40, 40, 0,40,40,40, 40])
    # mask = cv.filter2D(bw, cv.CV_8U, k)
    # cv.imshow("mask", mask)
    # cv.waitKey(0)
    # img = cv.bitwise_or(img, img, mask=mask)
    # img = cv.Sobel(img, cv.CV_8U, 1,1, ksize=3)
    #
    # thrs1 = 50
    # thrs2 = 150
    # edges = cv.Canny(bw,thrs1,thrs2,apertureSize = 3)
    # cv.imshow("edges", edges)
    # cv.waitKey(0)
    # minLineLength = 100
    # maxLineGap = 10
    # rho = 1
    # thresh = 50
    # lines = cv.HoughLinesP(edges, rho, np.pi/180, thresh, minLineLength, maxLineGap)
    #
    # if lines is None:
    #     lines = 0
    #
    # # Draw lines (for debugging purposes)
    # for x1,y1,x2,y2 in lines[0]:
    #     # if vp.filter_points(x1,y1,x2,y2) is False:  # Eliminate vertical lines that do not converge towards VP
    #     #     continue
    #         cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    #




    return img