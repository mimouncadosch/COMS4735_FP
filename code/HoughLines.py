import cv2 as cv
import numpy as np

class HoughLines(object):
    """docstring for HoughLines"""
    def __init__(self):
        super(HoughLines, self).__init__()
        # self.arg = arg

    def get_hough_lines(self, img):
        # Probabilistic Hough transform
        thrs1 = 100
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
            return img, lines


        # Draw lines (for debugging purposes)
        filtered_lines = []
        for x1,y1,x2,y2 in lines[0]:
            if self.filter_lines(x1,y1,x2,y2) is False:  # Filter lines that do not correspond to lanes
                continue
            # cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
            filtered_lines.append([x1,y1,x2,y2])
        return img, filtered_lines

    def filter_lines(self, x1, y1, x2, y2):
        if x1 - x2 == 0:
            return False
        slope = float(y1 - y2)/(x1 - x2)
        if slope <= -2.5:
            return True
        return False