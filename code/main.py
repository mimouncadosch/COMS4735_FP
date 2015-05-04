from feature_detection import *



def main():
    vp = VanishingPointFinder()
    cf = ColorFilterer()
    hl = HoughLines()
    ctf = ContourFinder()

    img = cv.imread("../data/lanes_5_medium.jpg")
    # img = cv.imread("../data/img_from_video.png")
    # # Resizing image
    # img = cv.resize(img, None, fx=0.3, fy=0.3, interpolation = cv.INTER_CUBIC)
    # img = feature_detection(vp, cf, hl, ctf, img)
    # cv.imshow("img", img)
    # cv.waitKey(0)
    # cap = cv.VideoCapture('../data/video_1.mp4')


    # while(cap.isOpened()):
    #     ret, frame = cap.read()
    #     frame = cv.resize(frame, None, fx=0.3, fy=0.3, interpolation = cv.INTER_CUBIC)
    #     frame = feature_detection(vp, cf, hl, ctf, frame)
    #     # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #     cv.imshow('frame',frame)
    #     if cv.waitKey(1) & 0xFF == ord('q'):
    #         break
    #
    # cap.release()
    # cv.destroyAllWindows()

    return True



if __name__ == "__main__":
    main()