import cv2 as cv
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster, fclusterdata

class Filter(object):
    """docstring for Filter"""
    def __init__(self):
        super(Filter, self).__init__()
        # self.arg = arg


    def filter_lines(self, img, lines):
        rows, cols = img.shape[:2]
        intercepts = []
        slopes = []


        # 1) For each line, find slope and intercept and store in arrays slopes and intercepts
        for x1, y1, x2, y2 in lines:
            cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

        # cv.imshow("img", img)
        # cv.waitKey(0)


        """
            slope = float(y2 - y1) / (x2 - x1)
            b = y1 - slope * x1
            # print slope, b

            slopes.append(slope)
            intercepts.append(b)

        diff_thresh = 300
        b1 = None
        b2 = None
        # Find intercept for each lane markingq
        sorted_intercepts = np.sort(intercepts)
        for i in range(len(intercepts)):
            if i+1 == len(intercepts):
                break
            if abs(sorted_intercepts[i+1] - sorted_intercepts[i]) > diff_thresh:
                b1 = sorted_intercepts[i]   # intercept first lane marking
                b2 = sorted_intercepts[i+1] # intercept second lane marking
                break

        if b1 is None or b2 is None:
            return img

        b1_id = np.max(np.where(intercepts == b1))
        b2_id = np.max(np.where(intercepts == b2))

        # # Find slope for each lane marking
        x1 = 0
        y1 = x1 * slopes[b1_id] + b1
        y2 = 0
        x2 = float(-1 * b1) / slopes[b1_id]
        x3 = 0
        y3 = x3 * slopes[b2_id] + b2
        x4 = float(-1 * b2) / slopes[b2_id]
        y4 = 0

        cv.line(img, (x1,int(y1)), (int(x2),y2), (0, 100,100), 10)
        cv.line(img, (x3,int(y3)), (int(x4),y4), (0, 100,100), 10)
        cv.imshow("Come on", img)
        cv.waitKey(0)

        """
        return img




    """
    def merge_lines(self, img, lines):  #, vp, vp_x
        Takes lines found by the Hough method and filters out the contours that do not correspond to lane markings.


        # 0) Setup
        rows, cols = img.shape[:2]
        slopes = np.zeros((len(lines    ), 1))           # list containing slope of remaining lines in image
        intercepts = []                                 # list of y-intercepts of remaining lines in image

        # 1) For each line, find slope and intercept of line.
        id = 0
        for x1, y1, x2, y2 in lines:
            # if vp.filter_points(x1,y1,x2,y2) is False:  # Eliminate vertical lines that do not converge towards VP
            #     continue
            # Slope m
            if x2 - x1 == 0:
                continue
            slope  = -1 * float(y2 - y1) / (x2 - x1)

            # y = mx + b => b = y - mx.
            # We can pick either (x1,y1) or (x2,y2), b will be the same
            b = y1 - slope * x1
            slopes[id, 0] = slope

            intercepts.append(b)
            id += 1


        # 2) Cluster the slopes into n_clusters clusters
        # fl = fclusterdata(slopes, 1)
        fl = fclusterdata(slopes,2,criterion='maxclust', metric='euclidean', depth=1, method='complete')
        n_clusters = np.max(fl)
        # print "number of clusters is %d ", n_clusters

        # 3) Merge the lines with the same slope
        # Take average of each cluster of lines with similar slope
        # Average of slope values for each cluster of lines
        tot_intercepts = []
        tot_slopes = []
            for l in range(1, n_clusters+1):    # For each cluster
                indices = np.where(fl == l)[0]  # Get indices of slopes that correspond to that cluster
                tot_intercepts.append(intercepts[indices[0]])
                tot_slopes.append(np.median(slopes[indices]))





        # for i in range(n_clusters):
        #     # y1 = x_left * m + b
        #     # y2 = x_right * m + b
        #     y1 = 0 * -tot_slopes[i] + abs(tot_intercepts[i])
        #     y2 = cols * -tot_slopes[i] + abs(tot_intercepts[i])
        #     # print y1
        #     print cols, y2
        #     cv.circle(img, (cols, int(y2)), 30, (0, 100, 100), 10)
        #     # cv.line(img, (0, int(y1)), (cols, int(y2)), (100, 100, 100), 5)
        #     cv.imshow("line", img)
        #     cv.waitKey(0)
        # 5) Plot the lines (for debugging purposes)
        # All lines pass through the center of gravity, where y = 0 and x = x_vp
        # y = m * x_vp + b  =>  b = - m * x_vp

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

        return img, slopes, intercepts  #tot_slopes

    def filter_lines(self, img, slopes, intercepts, vp_x):
        rows, cols = img.shape[:2]

        max_positive_slope = np.max(slopes)
        max_positive_slope_id = np.argmax(slopes)
        b1 = intercepts[max_positive_slope_id]
        y1 = abs(b1)

        cv.line(img, (0, int(y1)), (vp_x, 0), (0, 255, 0), 5)

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


        return img, max_positive_slope, min_negative_slope

    """