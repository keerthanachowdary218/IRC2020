import numpy as np
#import argparse
import imutils
import cv2
import freenect

#ap = argparse.ArgumentParser()
#ap.add_argument("-v", "--video", help="path to the (optional) video file")
#args = vars(ap.parse_args())
#greenLower=(0,0,0)
#greenUpper=(180,255,255)
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
 
greenLower = (32, 89, 8)
greenUpper = (64, 255, 255)

#if not args.get("video", False):
#camera = get_video()
#else:
#    camera = cv2.VideoCapture(args["video"])

while True:
    #(grabbed, frame) = camera.read()
    frame=get_video()
    #if args.get("video") and not grabbed:
    #    break

    #frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        print("x is ",x)
        print("y is ",y)
        if radius > 6:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.putText(frame,"baalll",(int(x),int(y)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)

    if key == 27:
        break

#frame.release()
cv2.destroyAllWindows()
