import numpy as np
import cv2 as cv
from VanishingPointFinder import *
from ColorFilterer import *
from HoughLines import *
from ContourFinder import *
from Filter import *

last_vp = [0, 0]
def feature_detection(vp, filter, hl, ctf, img):

    """
    Detects features in the image
    """
    # 0) Setup
    y_max, x_max, depth = img.shape
    # Black & white image
    bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 1) Find vanishing point and remove everything above horizon line
    # 1a) Get Hough lines with probabilistic method
    bw, lines = hl.get_hough_lines(bw, vp)

    if lines.shape[1] == 0: # Return if no Hough lines found
        return bw

    # 1b) Compute vanishing point VP(x, y)
    (x, y) = vp.compute_vanishing_point(lines, img.shape)

    # If no vanish point is found, use last found
    if np.isnan(x) or np.isnan(y):
        return bw
        # x = last_vp[0]
        # y = last_vp[1]

    # If vanish point is found, set it as precedent
    if (not np.isnan(x) and not np.isnan(y)):
        last_vp[0] = x
        last_vp[1] = y

    # 1c) Remove everything above horizon line
    bw = bw[y:y_max, 0:x_max]

    # (For debugging)
    cv.circle(bw, (int(x),0), 4, (0, 100, 100), 4)
    # cv.line(img, (0, int(y)), (x_max, int(y)), (0, 255, 200), 2) # Draw horizon line

    # 2) Merge lines found
    bw, slopes = filter.merge_lines(bw, lines, vp, int(x))

    # 3) Filter the merged lines
    bw = filter.filter_lines(bw, slopes, int(x))
    # cv.imshow("bw", bw)
    # cv.waitKey(0)
    # 3) Find contours and filter them
    # Send only a single channel of the image as findContours in OpenCV takes a single channel, 8-bit image
    # img = ctf.find_contours(bw, (int(x),int(y)))

    # cv.imshow("img", img)
    # cv.waitKey(0)
    # cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    # cv.imwrite("../test_images/horizon.jpg", img)
    return bw