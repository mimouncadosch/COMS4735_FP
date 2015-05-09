import cv2 as cv
import numpy as np

pos_array = []
clicks = 0
global_image = np.zeros((480, 271, 3))


def compute_transform_matrix(img):
    """
    This function computes and stores the transform matrix of an object from the world to the image plane.
    """
    # Correspondence (pixel <--> meters)
    # 100 pixels <--> 1 meter

    # Square selected in image has dimensions:
    # Width: 0.76 m x Length: 3.35 m
    # In pixels: 76 px x 335 px
    points = capture_points(img)
    src = np.array(points, dtype="float32")
    # dst = np.array([
    #         [0, 0],
    #         [76, 0],
    #         [76, 335],
    #         [0, 335]
    #                 ], dtype="float32")

    # Distances of diamond for transform_matrix2.npy
    dst = np.array([
            [0, 0],
            [400, 0],
            [400, 335],
            [0, 335]
                    ], dtype="float32")


    M = cv.getPerspectiveTransform(src, dst)

    np.save("transform_matrix2.npy", M)

    return True


def apply_transform(img):
    """
    This function applies the transform matrix to the image
    """
    M = np.load("transform_matrix2.npy")
    warped = cv.warpPerspective(img, M, (1000,1000))
    cv.imshow("warped", warped)
    cv.waitKey(0)

    points = capture_points(warped)


    return True


def capture_points(img):
    """
    Capture points in image
    """
    global global_image
    global pos_array

    global_image = img
    # cv.imshow("global_image", global_image)
    # cv.waitKey(0)

    cv.namedWindow("image")
    cv.setMouseCallback("image", capture_position)

    while (1):
        cv.imshow("image", global_image)
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()

    return pos_array


def capture_position(event, x, y, flags, param):
    global clicks
    global pos_array
    global global_image

    if event == cv.EVENT_LBUTTONDOWN:
        clicks += 1
        pos_array.append((x, y))
        cv.circle(global_image, (x, y), 1, (0, 255, 0), -1)
        print x, y
        # cv.imshow("gl", global_image)
        # cv.waitKey(0)
        # print "You have clicked (" + str(x) + ", "+str(y) + "). \n Press any key when you are done. \n Press ESC if you are lost."

    return False

