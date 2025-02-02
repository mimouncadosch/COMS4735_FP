import numpy as np
import math
from lines import line_intersection

class VanishingPointFinder(object):
    """VanishingPointFinder class"""
    def __init__(self):
        super(VanishingPointFinder, self).__init__()
        # self.arg = arg


    def compute_vanishing_point(self, lines, shape):
        # 1) Find slope and y-intercept of each line
        # A line can be expressed as y = mx + b, where m is the slope and b the y-intercept
        slopes = []     # list containing slope of all lines in image
        intercepts = [] # list of y-intercepts of all lines in image

        for x1,y1,x2,y2 in lines[0]:
            if self.filter_points(x1,y1,x2,y2) is False:  # Eliminate vertical lines
                continue

            # Slope m
            if x2 - x1 == 0:
                continue
            slope  = float(y2 - y1) / (x2 - x1)

            # y = mx + b => b = y - mx.
            # We can pick either (x1,y1) or (x2,y2), b will be the same
            b = y1 - slope * x1

            intercepts.append(b)
            slopes.append(slope)

        # 2) Extend line to edges of the image. This is equivalent to taking y = mx + b for x at left and right edges of the image
        n_lines = len(slopes)  # number of lines after filtering

        x_left = 0
        x_right = shape[1]
        y_extreme_vals = np.zeros([n_lines , 2]) # y values of each line at left and right edges of the image

        for i in range(n_lines):
            y_extreme_vals[i, 0] = slopes[i] * x_left + intercepts[i]
            y_extreme_vals[i, 1] = slopes[i] * x_right + intercepts[i]

        # 3) There are choose(n_lines, 2) possible intersections between the lines
        # Find the average point of intersection of all these possibilities

        n_inters = self.nCr(n_lines,2)
        # print "There are %d intersections", n_inters
        if n_inters == 0:
            return (np.nan, np.nan)


        inters = np.zeros([n_inters, 2])
        i = 0
        j = 1
        k = 0
        while i < n_lines:
            while j < n_lines:
                # Line 1 (i)
                p1_left = np.array([x_left, y_extreme_vals[i, 0]])
                p1_right = np.array([x_right, y_extreme_vals[i, 1]])

                # Line 2 (j)
                p2_left = np.array([x_left,y_extreme_vals[j,0]])
                p2_right = np.array([x_right,y_extreme_vals[j,1]])

                x, y = line_intersection(p1_left, p1_right, p2_left, p2_right)
                inters[k,0] = x
                inters[k,1] = y
                # cv.circle(img, (int(x),int(y)), 5, (0, 100, 100), 2)
                j+=1
                k+=1
            i+=1
            j=i+1

        # 4) Eliminate zero values and return
        inters = inters[~np.all(inters == 0, axis=1)]
        inters_x = inters[:,0]
        inters_y = inters[:,1]

        # TODO: explain m: values that are more than m standard deviations away from mean are discarded
        m = 2
        inters_x = inters_x[abs(inters_x - np.mean(inters_x)) < m * np.std(inters_x)]
        inters_y = inters_y[abs(inters_y - np.mean(inters_y)) < m * np.std(inters_y)]

        vp_x = np.mean(inters_x)
        vp_y = np.mean(inters_y)

        ## Draw extended lines (for debugging)
        # for i in range(n_lines):
        #     p1 = (x_left, int(y_extreme_vals[i,0]))
        #     p2 = (x_right, int(y_extreme_vals[i, 1]))
        #     cv.line(img, p1, p2, (0, 255, 0))

        # cv.imwrite("../test_images/extended_lines_4_27.jpg", img)

        return (vp_x, vp_y)

    def nCr(self, n,r):
        """
        Function: n choose k
        """
        if not n > 2:
            return 0
        f = math.factorial
        return f(n) / f(r) / f(n-r)

    def filter_points(self, x1, y1, x2, y2):
        """
        Eliminates vertical lines that do not point towards the vanishing point
        """
        thresh_x = 5    # x values of two enpoints of line need to be more than thresh_x pixels away from each other
        thresh_y = 2    # analogous for y
        if abs(x1 - x2) <= thresh_x or abs(y1 - y2) <= thresh_y:
            return False
        return True