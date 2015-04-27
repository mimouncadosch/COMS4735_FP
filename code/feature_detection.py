import numpy as np
import cv2 as cv
from VanishingPointFinder import *

def feature_detection():

    img = cv.imread("../data/lanes_3.jpg")

    # cv.imshow("image", img)
    # cv.waitKey(0)

    # Color ranges
    # OpenCV is BGR
    white_lb = (180, 100, 0)
    white_ub = (255, 255, 255)
    yellow_lb = (0, 165, 130)
    yellow_ub = (150, 255, 255)

    # Masks for color filtering
    color_mask_white = cv.inRange(img, white_lb, white_ub)
    color_mask_yellow = cv.inRange(img, yellow_lb, yellow_ub)

    white_filtered_img = cv.bitwise_and(img, img, mask = color_mask_white)
    yellow_filtered_img = cv.bitwise_and(img, img, mask = color_mask_yellow)

    # Combined image
    img = cv.bitwise_or(white_filtered_img, yellow_filtered_img, mask=None)

    shape = img.shape

    # Probabilistic Hough transform
    vp = VanishingPointFinder()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize = 3)
    minLineLength = 100
    maxLineGap = 10
    rho = 1
    thresh = 50
    lines = cv.HoughLinesP(edges, rho, np.pi/180, thresh, minLineLength, maxLineGap)

    # Draw lines (for debugging purposes)
    # for x1,y1,x2,y2 in lines[0]:
    #     if vp.filter_points(x1,y1,x2,y2) is False:  # Eliminate vertical lines that do not converge towards VP
    #         continue
    #     cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    (x, y) = vp.compute_vanishing_point(lines, shape, img)

    #


    # cv.imshow("color filtered", img)
    # cv.waitKey(0)

    """
    k = np.array([-1, 0, 1])
    k_row = np.array([-1, 0, 1])
    for i in range(5):
        k = np.vstack((k, k_row))

    k = np.transpose(k)
    img = cv.filter2D(img, cv.cv.CV_8U, kernel=k)
    """


    """
    rho = 1
    lines = cv.HoughLines(img[:,:,0], rho, np.pi/ 180, 1500)

    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    """



    """
    # Sobel filter for horizontal derivative (rate of change along x axis)
    img = cv.Sobel(img, cv.cv.CV_8U, 1, 0, ksize=1)
    """

    # cv.imshow("img_filtered", img)
    # cv.waitKey(0)

    # cv.imwrite("../test_images/color_filtered_4_24.jpg", img)
    return True