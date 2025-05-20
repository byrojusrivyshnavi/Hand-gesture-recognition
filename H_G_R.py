import numpy as np
import cv2
import time
import os
import webbrowser

try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("text to speech test")
    engine.runAndWait()
except Exception as e:
    print("Text to speech failed:",e)
    engine=None
cap = cv2.VideoCapture(0)# creating the videocapture object# and reading from the input file# Change it to 0 if reading from webcam # video capture 

prev_frame_time = 0# used to record the time when we processed last frame

new_frame_time = 0# used to record the time at which we processed current frame

while(cap.isOpened()):# Reading the video file until finished
    ret, frame = cap.read()# Capture frame-by-frame
    if not ret:# if video finished or no Video Input
        break
    blurred_frame=cv2.GaussianBlur(frame,(5,5),0)
    hsv=cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    ret,thresh = cv2.threshold(gray,127,255,0)
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([120,255,250])
    mask=cv2.inRange(hsv, lower_blue, upper_blue)
    
    gray = cv2.resize(gray, (500, 300))# resizing the frame size according to our need
    font = cv2.FONT_HERSHEY_SIMPLEX# font which we will be using to display FPS
    new_frame_time = time.time()# time when we finish processing for this frame
    fps = 1/(new_frame_time-prev_frame_time)# Calculating the fps# fps will be number of frame processed in given time frame# since their will be most of time error of 0.001 second# we will be subtracting it to get more accurate result
    prev_frame_time = new_frame_time
    fps = int(fps)# converting the fps into integer
    fps = str(fps)# converting the fps to string so that we can display it on frame# by using putText function
    #cv2.putText(gray, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame

    contours,_=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area=cv2.contourArea(contour)
        M=cv2.moments(thresh)
        if area>15000:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 4)
            cv2.drawContours(frame, contour, -1,(0,255,0),3)
            # get the min area rect
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            # convert all coordinates floating point values to int
            box = np.int0(box)
            # draw a red 'nghien' rectangle
            cv2.drawContours(frame, [box], 0, (0, 0, 255))
            # finally, get the min enclosing circle
            (x, y), radius = cv2.minEnclosingCircle(contour)
            # convert all values to int
            center = (int(x), int(y))
            radius = int(radius)
            # and draw the circle in blue
            Frame = cv2.circle(frame, center, radius, (255, 0, 0), 2)
            

            #print('what shape is current')
            #print(input("enter shape code"))
            
            print(radius)
            if 150<=radius>=155:
                cv2.putText(frame, '1', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("1")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
            elif 141<=radius>=147:
                cv2.putText(frame, '2', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("2")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
            elif 230<=radius>=235:
                cv2.putText(frame, '3', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("3")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
            elif 203<=radius>=209:
                cv2.putText(frame, '4', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("4")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
            elif 141<=radius>=147:
                cv2.putText(frame, '5', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("5")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 126<=radius>=129:
                cv2.putText(frame, 'A', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("A")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 160<=radius>=166:
                cv2.putText(frame, 'B', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("B")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 162<=radius>=167:
                cv2.putText(frame, 'C', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("C")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 149<=radius>=157:
                cv2.putText(frame, 'D', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("D")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 101<=radius>=104:
                cv2.putText(frame, 'E', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("E")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 190<=radius>=195:
                cv2.putText(frame, 'F', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("F")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 150<=radius>=156:
                cv2.putText(frame, 'G', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("G")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 195<=radius>=200:
                cv2.putText(frame, 'H', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("H")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 170<=radius>=172:
                cv2.putText(frame, 'I', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("I")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 100<=radius>=105:
                cv2.putText(frame, 'J', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("J")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 142<=radius>=147:
                cv2.putText(frame, 'K', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("K")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 91<=radius>=93:
                cv2.putText(frame, 'L', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("L")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 142<=radius>=144:
                cv2.putText(frame, 'M', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("M")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 145<=radius>=147:
                cv2.putText(frame, 'N', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("N")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 165<=radius>=169:
                cv2.putText(frame, 'O', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("O")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 136<=radius>=138:
                cv2.putText(frame, 'P', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("P")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 157<=radius>=160:
                cv2.putText(frame, 'Q', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("Q")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 163<=radius>=172:
                cv2.putText(frame, 'R', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("R")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 142<=radius>=145:
                cv2.putText(frame, 'S', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("S")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 124<=radius>=127:
                cv2.putText(frame, 'T', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("T")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 173<=radius>=175:
                cv2.putText(frame, 'U', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("U")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 168<=radius>=170:
                cv2.putText(frame, 'V', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("V")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 133<=radius>=135:
                cv2.putText(frame, 'W', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("W")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 141<=radius>=145:
                cv2.putText(frame, 'X', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("X")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 169<=radius>=172:
                cv2.putText(frame, 'Y', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("Y")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
            elif 151<=radius>=154:
                cv2.putText(frame, 'Z', (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)# putting the FPS count on the frame
                engine.say("Z")# play the speech
                engine.runAndWait()
                #url='Alarm and clock'
                #webbrowser.open(url)
               #displaying the frame with fps
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):# press 'Q' if you want to exit
        break
engine.runAndWait()
cap.release()# When everything done, release the capture
cv2.destroyAllWindows()# Destroy the all windows now