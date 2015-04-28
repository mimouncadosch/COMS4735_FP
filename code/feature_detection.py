import numpy as np
import cv2 as cv
from VanishingPointFinder import *
from ColorFilterer import *
from HoughLines import *
from ContourFinder import *

def feature_detection():
    vp = VanishingPointFinder()
    cf = ColorFilterer()
    hl = HoughLines()
    ctf = ContourFinder()
    """
    Detects features in the image
    """
    img = cv.imread("../data/lanes_3_medium.jpg")

    # cv.imshow("image", img)
    # cv.waitKey(0)

    # 1) Find vanishing point and remove everything above horizon line
    y_max, x_max, depth = img.shape
    lines = hl.get_hough_lines(img)

    (x, y) = vp.compute_vanishing_point(lines, img.shape)
    # Remove everything above horizon line
    img = img[y:y_max, 0:x_max]

    # (For debugging)
    # cv.circle(img, (int(x),int(y)), 4, (0, 100, 100), 2)
    # cv.line(img, (0, int(y)), (x_max, int(y)), (0, 255, 200), 2) # Draw horizon line

    # 2) Filter image by colors of lane markings (white and yellow)
    img = cf.filter_by_color(img)

    # 3) Find contours
    # Send only a single channel of the image as findContours in OpenCV takes a single channel, 8-bit image
    ctf.find_contours(img)


    # cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    #


    # cv.imwrite("../test_images/horizon.jpg", img)
    return True