from feature_detection import *
from perspective_projection import *
from feature_extraction import *

def main():
    vp = VanishingPointFinder()
    cf = ColorFilterer()
    hl = HoughLines()
    ctf = ContourFinder()
    filter = Filter()

    # Test Images
    # filename = "../data/calibration_images/calibration3.jpg"
    # filename = "../data/road.jpg"
    # filename = "../data/img_from_video_2.png"
    # filename = "../data/lane_right.png"
    # img = cv.imread(filename)
    # img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

    # 1) Compute perspective projection transform
    t_number = 7
    # compute_transform_matrix(img, t_number)

    # 2) Apply transform to image at hand
    # cv.imshow("img", img)
    # cv.waitKey(0)
    #
    # img = apply_transform(img, t_number)
    # cv.imshow("warped", img)
    # cv.waitKey(0)
    #
    # img = extract_features(img, hl, vp)

    # cv.imshow("img", img)
    # cv.waitKey(0)


    cap = cv.VideoCapture('../data/video_3_trimmed_steering.mp4')
    cv.namedWindow("video_org")
    cv.namedWindow("video_warped")
    while(cap.isOpened()):
        ret, frame = cap.read()
        # frame = cv.resize(frame, None, fx=0.3, fy=0.3, interpolation = cv.INTER_CUBIC)
        cv.imshow('video_org',frame)
        frame = apply_transform(frame, t_number)
        frame = extract_features(frame, hl, vp)
        # frame = feature_detection(vp, filter, hl, ctf, frame)
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # extract_features(frame, hl, vp)
        cv.imshow('video_warped',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv.destroyAllWindows()



    return True



if __name__ == "__main__":
    main()
