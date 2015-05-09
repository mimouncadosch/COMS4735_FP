from feature_detection import *
from perspective_projection import *

def main():
    vp = VanishingPointFinder()
    cf = ColorFilterer()
    hl = HoughLines()
    ctf = ContourFinder()
    filter = Filter()

    # Test Images
    # img = cv.imread("../data/lane_right.png")
    # img = cv.imread("../data/img_from_video_2.png")
    # img = cv.imread("../data/img_from_video_medium.png")
    # cv.imshow("img", img)
    # cv.waitKey(0)
    # img = cv.imread("../data/lanes_5_medium.jpg")
    # img = cv.imread("../data/lanes_4_medium.jpg")
    img = cv.imread("../data/calibration.jpg")
    img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

    # cv.imshow("img resized", img)
    # cv.waitKey(0)
    # img = cv.imread("../data/img_from_video.png")
    # # Resizing image
    # img = cv.resize(img, None, fx=0.3, fy=0.3, interpolation = cv.INTER_CUBIC)

    # 1) Compute perspective projection transform
    # Only required once
    # compute_transform_matrix(img)

    # 2) Apply transform to image at hand
    apply_transform(img)


    # img = feature_detection(vp, filter, hl, ctf, img)
    # cv.imshow("img", img)
    # cv.waitKey(0)
    """
    cap = cv.VideoCapture('../data/video_2.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = cv.resize(frame, None, fx=0.3, fy=0.3, interpolation = cv.INTER_CUBIC)
        frame = feature_detection(vp, filter, hl, ctf, frame)
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
    """

    return True



if __name__ == "__main__":
    main()
