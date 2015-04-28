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

        max_perim_id = -1
        max_perim = -1
        for i in xrange(0,len(contours)):
            perim = cv.arcLength(contours[i], True)
            if(perim >= max_perim):
                max_perim = perim
                max_perim_id = i

        epsilon = 0.01 * max_perim
        print max_perim


        for i in range(len(contours)):
        # if len(contours) > 0:
            ctr_color = (0, 250, 0)
            cv.drawContours(img, contours, i, ctr_color, 5,8)
            area = cv.contourArea(contours[i])
            print area
        cv.imshow("contours", img)
        cv.waitKey(0)
        return True