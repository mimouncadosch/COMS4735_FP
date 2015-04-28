import cv2 as cv
import numpy as np

class HoughLines(object):
    """docstring for HoughLines"""
    def __init__(self):
        super(HoughLines, self).__init__()
        # self.arg = arg

    def get_hough_lines(self, img):
        # Probabilistic Hough transform
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
        # cv.imshow("img", img)
        # cv.waitKey(0)
        return lines
