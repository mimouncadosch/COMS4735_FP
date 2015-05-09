import cv2 as cv
import numpy as np

class HoughLines(object):
    """docstring for HoughLines"""
    def __init__(self):
        super(HoughLines, self).__init__()
        # self.arg = arg

    def get_hough_lines(self, img, vp):

        # cv.imshow("img b/f hough", img)
        # cv.waitKey(0)
        # filtered = cv.Sobel(img, cv.CV_8U, 1, 0)
        # cv.imshow("img a/f thresh", img)
        # cv.waitKey(0)

        # Probabilistic Hough transform
        thrs1 = 50
        thrs2 = 150
        edges = cv.Canny(img,thrs1,thrs2,apertureSize = 3)
        # cv.imshow("edges", edges)
        # cv.waitKey(0)
        minLineLength = 100
        maxLineGap = 10
        rho = 1
        thresh = 50
        lines = cv.HoughLinesP(edges, rho, np.pi/180, thresh, minLineLength, maxLineGap)

        if lines is None:
            lines = 0

        # Draw lines (for debugging purposes)
        for x1,y1,x2,y2 in lines[0]:
            if vp.filter_points(x1,y1,x2,y2) is False:  # Eliminate vertical lines that do not converge towards VP
                continue
            cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

        return img, lines
