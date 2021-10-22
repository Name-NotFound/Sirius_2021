import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())

camera = cv2.VideoCapture(0) if not args.get("video", False) else cv2.VideoCapture(args["video"])


while True:
    (grabbed, frame) = camera.read()
    if args.get("video") and not grabbed:
        break

    detected_circles = cv2.HoughCircles(cv2.blur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (3, 3)),
                                        cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                        param2=30, minRadius=1, maxRadius=40)

    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
