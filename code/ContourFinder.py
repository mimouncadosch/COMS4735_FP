import cv2 as cv
import numpy as np
class ContourFinder(object):
    """docstring for ContourFinder"""
    def __init__(self):
        super(ContourFinder, self).__init__()
        # self.arg = arg


    def find_contours(self, img, vp):
        """
        Find and draw contours in image
        """

        # 1) De-noise the image by erosion
        kernel = np.ones((5,5),np.uint8)
        img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

        # cv.imshow("eroded", img)
        # cv.waitKey(0)

        # 2) Apply a binary mask and retrieve contours
        lb = (1, 1, 1)
        ub = (255, 255, 255)
        mask = cv.inRange(img, lb, ub)
        img = cv.bitwise_and(img,img,mask = mask)

        contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE, (0,0))

        ctr_color = (0, 250, 0)
        epsilon = 0.01
        areas = np.zeros([len(contours), 1])

        # 3) Find contours with largest areas
        for i in range(len(contours)):
            # cv.drawContours(img, contours, i, ctr_color, 5,8)
            area = cv.contourArea(contours[i])
            areas[i] = area

        # Index of top three contours with largest areas
        top = np.argsort(areas, axis=0)[::-1][0:3]

        # 4) (For debugging): draw largest contours found, and draw lines passing through them
        # for t in top:
        #     cv.drawContours(img, contours, t, ctr_color, 5,8)

        self.filter_contours(contours, top, vp, img)
        return contours


    def filter_contours(self, contours, top_index, vp, img):
        """
        Takes contours found by find_contours and filters out the contours that do not correspond to lane markings.
        This function filters as lane markings should converge towards the vanishing point
        top_index: index of contours with largest areas
        """

        rows, cols = img.shape[:2]

        slopes = []         # list containing slope of remaining lines in image
        intercepts = []     # list of y-intercepts of remaining lines in image
        lane_ids = []       # indices of lines that do correspond to lanes
        # 1) For each line, find slope and intercept of line.

        for i in range(len(top_index)):
            [vx,vy,x,y] = cv.fitLine(contours[top_index[i]], cv.cv.CV_DIST_L2,0,0.01,0.01)

            # Slope m
            m = float(vy)/vx
            # y  = m * x + b => b = y - m * x
            b = y - m * x
            slopes.append(m[0])
            intercepts.append(b[0])

            # 2) For each line check if y = m * vp_x + b = 0
            # To check for y = 0, use threshold
            # TODO: justify thresh
            thresh = 5  # pixels
            y = m * vp[0] + b
            if abs(y) <= thresh:
                lane_ids.append(i)

        # 3) Draw only the lane markings
        for id in lane_ids:
            print id
            p1 = (0, int(intercepts[id]))
            p2 = (cols, int(slopes[id]*cols + intercepts[id]))

            cv.line(img, p1, p2, (0, 200, 200), 5)


        cv.imshow("contours", img)
        cv.waitKey(0)
        return True