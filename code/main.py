from feature_detection import *
import time

def main():
    start_time = time.time()
    vp = VanishingPointFinder()
    cf = ColorFilterer()
    hl = HoughLines()
    ctf = ContourFinder()
    filter = Filter()

    img = cv.imread("../data/lanes_3_small.jpg")

    #print("Initializing Objects %s --- " % (time.time() - start_time))
    #start_time2 = time.time()
    # img = cv.imread("../data/img_from_video_2_medium.png")
    # img = cv.imread("../data/img_from_video_medium.png")
    # img = cv.imread("../data/lanes_5_medium.jpg")
    #print("Reading Image %s --- " % (time.time() - start_time2))

    # img = cv.imread("../data/img_from_video.png")
    # # Resizing image
    # img = cv.resize(img, None, fx=0.3, fy=0.3, interpolation = cv.INTER_CUBIC)
    """
    img = feature_detection(vp, filter, hl, ctf, img)
    cv.imshow("img", img)
    cv.waitKey(0)
    """
    i = 0
    cap = cv.VideoCapture('../data/video_2.mp4')
    while(cap.isOpened()):
        i += 1
        ret, frame = cap.read()
        frame = cv.resize(frame, None, fx=0.3, fy=0.3, interpolation = cv.INTER_CUBIC)
        frame = feature_detection(vp, filter, hl, ctf, frame)
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	#if i % 2 == 0:
        	#cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    	print("While loop %s --- " % (time.time() - start_time))
	start_time = time.time()
	
    cap.release()
    cv.destroyAllWindows()

    return True



if __name__ == "__main__":
    main()
