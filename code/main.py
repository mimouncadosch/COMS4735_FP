from feature_detection import *
from perspective_projection import *

def main():
    vp = VanishingPointFinder()
    cf = ColorFilterer()
    hl = HoughLines()
    ctf = ContourFinder()
    filter = Filter()

    # Test Images
    # filename = "../data/calibration_images/calibration3.jpg"
    filename = "../data/road.jpg"

    img = cv.imread(filename)
    # img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

    # 1) Compute perspective projection transform
    t_number = 7
    # compute_transform_matrix(img, t_number)

    # 2) Apply transform to image at hand
    cv.imshow("img", img)
    cv.waitKey(0)

    img = apply_transform(img, t_number)
    cv.imshow("warped", img)
    cv.waitKey(0)

    # img = feature_detection(vp, filter, hl, ctf, img)
    # cv.imshow("img", img)
    # cv.waitKey(0)


    """
    cap = cv.VideoCapture('../data/video_2.mp4')

    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = cv.resize(frame, None, fx=0.3, fy=0.3, interpolation = cv.INTER_CUBIC)
        frame = apply_transform(frame)
        # frame = feature_detection(vp, filter, hl, ctf, frame)
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
