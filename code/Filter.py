import cv2 as cv
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster, fclusterdata

class Filter(object):
    """docstring for Filter"""
    def __init__(self):
        super(Filter, self).__init__()
        # self.arg = arg

    def merge_lines(self, img, lines, vp, vp_x):
        """
        Takes lines found by the Hough method and filters out the contours that do not correspond to lane markings.
        """

        # 0) Setup
        rows, cols = img.shape[:2]
        slopes = np.zeros((len(lines[0]), 1))           # list containing slope of remaining lines in image
        intercepts = []                                 # list of y-intercepts of remaining lines in image

        # 1) For each line, find slope and intercept of line.
        id = 0
        for x1, y1, x2, y2 in lines[0]:
            if vp.filter_points(x1,y1,x2,y2) is False:  # Eliminate vertical lines that do not converge towards VP
                continue
            # Slope m
            if x2 - x1 == 0:
                continue
            slope  = -1 * float(y2 - y1) / (x2 - x1)

            # y = mx + b => b = y - mx.
            # We can pick either (x1,y1) or (x2,y2), b will be the same
            b = y1 - slope * x1
            slopes[id, 0] = slope
            # slopes.append(slope)
            intercepts.append(b)
            id += 1

        """
        # 2) Eliminate zero values from the slopes vector
        n_zeros = np.where(slopes == 0)
        if len(n_zeros[0]) > 0:
            first_zero_val = np.min(np.where(slopes == 0)[0])
            slopes = slopes[0:first_zero_val, :]
        """
        """
        # 3) Cluster the slopes into n_clusters clusters
        fl = fclusterdata(slopes, 1)
        n_clusters = np.max(fl)
        # print "number of clusters is %d ", n_clusters

        # 4) Merge the lines with the same slope
        # Take average of each cluster of lines with similar slope
        # Average of slope values for each cluster of lines
        tot_slopes = np.zeros((1, n_clusters))
        for l in range(1, n_clusters+1):    # For each cluster
            indices = np.where(fl == l)[0]  # Get indices of slopes that correspond to that cluster
            tot_slopes[0, l-1] = np.mean(slopes[indices])

        """
        # 5) Plot the lines (for debugging purposes)
        # All lines pass through the center of gravity, where y = 0 and x = x_vp
        # y = m * x_vp + b  =>  b = - m * x_vp
        """
        for s in tot_slopes[0]:
            # If slope > 0, line must pass through left side of image, and vanishing point
            b = - s * vp_x
            # If slope is positive, line passes through left edge of the image
            # y = m * 0 + b
            if s > 0:
                y = abs(b)
                cv.line(img, (0, int(y)), (vp_x, 0), (100, 100, 100), 5)
            # If slope is negative, line passes through right edge of the image
            # y = m * x_right + b
            if s < 0:
                y = abs(s * cols + b)
                cv.line(img, (cols, int(y)), (vp_x, 0), (100, 100, 100), 5)
        """
        return img, slopes, intercepts  #tot_slopes

    def filter_lines(self, img, slopes, intercepts, vp_x):
        rows, cols = img.shape[:2]

        max_positive_slope = np.max(slopes)
        max_positive_slope_id = np.argmax(slopes)
        b1 = intercepts[max_positive_slope_id]
        y1 = abs(b1)

        cv.line(img, (0, int(y1)), (vp_x, 0), (0, 255, 0), 5)
        """
        pos_slopes = np.where(slopes > 0)
        print intercepts
        if len(slopes[pos_slopes]) > 0:
            max_positive_slope = np.max(slopes[pos_slopes])
            # b1 = np.argmax(intercepts[pos_slopes])
            # b1 = - max_positive_slope * vp_x
            # y1 = abs(b1)
            # cv.line(img, (0, int(y1)), (vp_x, 0), (0, 255, 0), 5)
        else:
            max_positive_slope = np.nan

        neg_slopes = np.where(slopes < 0)
        if len(slopes[neg_slopes])  > 0:
            min_negative_slope = np.min(slopes[neg_slopes])
            b2 = - min_negative_slope * vp_x
            y2 = abs(min_negative_slope * cols + b2)
            cv.line(img, (cols, int(y2)), (vp_x, 0), (0, 255, 0), 5)
        else:
            min_negative_slope = np.nan
        """

        return img, max_positive_slope, min_negative_slope