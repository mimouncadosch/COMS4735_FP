import cv2 as cv
import numpy as np
from HoughLines import *

class ColorFilterer(object):
    """docstring for ColorFilterer"""
    def __init__(self):
        super(ColorFilterer, self).__init__()
        # self.arg = arg

    def filter_by_color(self, img):
        """
        Filter image by color for the colors of the lane markings
        """
        # Filter image by color
        # Color ranges
        # OpenCV is BGR
        white_lb = (180, 170, 170)
        white_ub = (255, 255, 255)
        yellow_lb = (0, 160, 200)
        yellow_ub = (150, 255, 255)
        yellow_lb = (0, 80, 100)
        yellow_ub = (150, 255, 255)


        # Masks for color filtering
        # color_mask_white = cv.inRange(img, white_lb, white_ub)
        # color_mask_yellow = cv.inRange(img, yellow_lb, yellow_ub)

        # cv.imshow("color mask yellow", color_mask_yellow)
        # cv.waitKey(0)

        # white_filtered_img = cv.bitwise_and(img, img, mask = color_mask_white)
        # yellow_filtered_img = cv.bitwise_and(img, img, mask = color_mask_yellow)
        # cv.imshow("yw filtered", yellow_filtered_img)
        # cv.waitKey(0)
        # 1) Erode yellow to get rid of green
        # kernel = np.ones((5,5),np.uint8)
        # yellow_filtered_img = cv.erode(yellow_filtered_img, kernel, iterations=1)

        # 2) Apply linear filter to yellow image to get rid of sky
        # kernel_two = np.array([-1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1])
        # kernel = np.array([-1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1])
        # kernel = np.array([-1, 0, 1])
        # white_filtered_img = cv.filter2D(white_filtered_img, cv.CV_8U, kernel_two)

        # 3) Combine image
        # img = cv.bitwise_or(white_filtered_img, yellow_filtered_img, mask=None)
        # img = cv.bitwise_or(img, img, mask=color_mask_yellow)


        # # 4) Sobel operator get edges
        # img = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=1)
        # kernel_two = np.array([-100, -100, -100, -100, -100, 0, 0, 100, 100, 100, 100, 100])
        # kernel_two = np.array([-255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255])

        # cv.imshow("yellow filtered", img)
        # cv.waitKey(0)
        # img = cv.filter2D(img, cv.CV_8U, kernel_two)
        # img = cv.Sobel(img, cv.CV_8U, 3, 1, ksize=5)
        # cv.imshow("yellow filtered", img)
        # cv.waitKey(0)
        # img = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        # cv.imshow("a/f filter", img)
        # cv.waitKey(0)


        # number of horizontal image "slices"
        # print img.shape
        # n_rows = 8
        # row_size = 60
        # cv.imshow("img b/f slicing", img)
        # cv.waitKey(0)

        # k_width = 20
        # hl = HoughLines()
        # for r in range(n_rows):
        #     r = n_rows - (r + 1)
        #     row = img[r*row_size:(r+1)*row_size, :]
        # k = self.kernel(k_width)
        #     # print k_width
        #     k_width = k_width - 1

        # color_mask_yellow = cv.inRange(img, yellow_lb, yellow_ub)

        # cv.imshow("row " + str(r), row)
        # cv.waitKey(0)


        # yellow_filtered_img = cv.erode(yellow_filtered_img, kernel, iterations=1)

        # k_width -= 1

        #
        # k = np.ones((5,5),np.uint8)
        # row = cv.threshold(row, 100, )
        # row = cv.adaptiveThreshold(row, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 3, 100)
        # row = cv.morphologyEx(row, cv.MORPH_CLOSE, k)
        # row = cv.Sobel(row, cv.CV_8U, 0, 1, ksize=3)

        #
        #

        # color_mask_white = cv.inRange(row, white_lb, white_ub)
        # white_filtered_img = cv.bitwise_and(row, row, mask=color_mask_white)
        # color_mask_yellow = cv.inRange(row, yellow_lb, yellow_ub)
        # row = cv.bitwise_and(row, row, mask=color_mask_yellow)
        # row = cv.bitwise_or(white_filtered_img, yellow_filtered_img, mask=None)

        # row = cv.filter2D(row, cv.CV_8U, k)

        # cv.imshow("row " + str(r), row)
        # cv.waitKey(0)

        # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # k = np.ones((15,15),np.uint8)
        # bw = cv.morphologyEx(bw, cv.MORPH_CLOSE, k)
        # bw = cv.Sobel(bw, cv.CV_8U, 0, 1, ksize=1)

        # lines = hl.get_hough_lines(img)

        # if len(lines) > 0:
        #     for x1,y1,x2,y2 in lines[0]:
        #         cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

        # cv.imshow("img", img)
        # cv.waitKey(0)

        return img


    def kernel(self, span):
        if span < 0:
            span = 0
        """
        Creates a linear kernel with variable number of -1, 0, 1
        :param span:
        :return:
        """
        ones = np.ones([1, span], np.uint8)
        zeros = np.zeros([1, 1], np.uint8)

        kernel = np.hstack((ones*-1, zeros))
        kernel = np.hstack((kernel, ones))
        print kernel
        return kernel