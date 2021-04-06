# Author: Kartik Bharadwaj

import cv2
import numpy as np
import argparse

def main():
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--min-area", type=int, default=10, help="minimum area size")
    args = vars(ap.parse_args())
    
    cap = cv2.VideoCapture('F:\softwares\goodrot.avi')
    fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
    if cap.isOpened() == False:
        print "error: Not able to access video\n"
        break
  	      
    while cv2.waitKey(1)!= 27 and cap.isOpened():
        ret, imgOriginal = cap.read()
        
        if not imgOriginal is None:
            print "error: no frame read from camera\n"
            break
        
        imgBGR = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)
        imgBGR = cv2.GaussianBlur(imgBGR, (15,15), 0)
                
        fgmask = fgbg.apply(imgBGR)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        
        thresh = cv2.dilate(thresh, None, iterations=10)
        (_, contours, hierachy) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in contours:
            
            if cv2.contourArea(c) < args["min_area"]:
                continue
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imgOriginal, (x, y), (x + w, y + h), (0,255,0), 2)
            time.sleep(0.5)
            print "X %d" %(cX),",Y %d" %(cY)
            cv2.imshow("Trackedfinal", imgOriginal)
                            
    cap.release()        
    cv2.destroyAllWindows()

#######################################################################################
if __name__ == "__main__":
    main()