import cv2 as cv
import numpy as np
class ContourFinder(object):
    """docstring for ContourFinder"""
    def __init__(self):
        super(ContourFinder, self).__init__()
        # self.arg = arg


    def find_contours(self, img):
        """
        Find and draw contours in image
        """
        kernel = np.ones((5,5),np.uint8)
        img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

        cv.imshow("eroded", img)
        cv.waitKey(0)

        lb = (1, 1, 1)
        ub = (255, 255, 255)
        mask = cv.inRange(img, lb, ub)
        img = cv.bitwise_and(img,img,mask = mask)

        contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE, (0,0))

        ctr_color = (0, 250, 0)
        areas = np.zeros([len(contours), 1])
        for i in range(len(contours)):
            # cv.drawContours(img, contours, i, ctr_color, 5,8)
            area = cv.contourArea(contours[i])
            areas[i] = area

        # # Top two areas
        top = np.argsort(areas, axis=0)[::-1][0:2]

        ctr_color = (0, 250, 0)
        for t in top:
            cv.drawContours(img, contours, t, ctr_color, 5,8)

        cv.imshow("contours", img)
        cv.waitKey(0)
        return True