import keyboard
def Volume_gesture():
    import cv2
    import time
    import numpy as np
    import HandTrackingModule as htm
    import math
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

    # variables
    wCam,hCam=1280,720
    cap=cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)
    pTime=0
    detector=htm.handDetector(detectionCon=0.7)

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # volume.GetMute()
    # volume.GetMasterVolumeLevel()
    volRange = volume.GetVolumeRange()
    minVol = volRange[0]
    maxVol = volRange[1]
    vol = 0
    volBar = 400
    volPer = 0
    while True:
        success,img=cap.read()
        img=cv2.flip(img,1)
        img=detector.findHands(img)
        lmlist=detector.findPosition(img,draw=False)
        
        if len(lmlist) != 0:    
            # print(lmlist[4],lmlist[8])
            # x1,y1=lmlist[4][1],lmlist[4][2]
            x2,y2=lmlist[8][1],lmlist[8][2]
            cx,cy=(x2)//2,(y2)//2
            # length=math.hypot(x2,y2)
            # print(length)

            # cv2.circle(img,(x1,y1), 15,(255,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2), 15,(255,0,255),cv2.FILLED)
            # cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
            cv2.circle(img,(cx,cy), 15,(255,0,255),cv2.FILLED)

            # vol = np.interp(length, [30, 270], [minVol, maxVol])
            # volBar = np.interp(length, [30, 270], [400, 150])
            # volPer = np.interp(length, [30, 270, [0, 100])
            # print(vol)
            # volume.SetMasterVolumeLevel(vol, None)
            

            # if length<30:
            #     cv2.circle(img,(cx,cy), 15,(0,0,0),cv2.FILLED)
            # elif length>270:
            #     cv2.circle(img,(cx,cy), 15,(0,0,0),cv2.FILLED)
            
        # cv2.rectangle(img, (30, 150), (85, 400), (255, 0, 0), 3)
        # cv2.rectangle(img, (30, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
        # cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 3)
        # other
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,f"fps:{int(fps)}",(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
        
        
        if keyboard.is_pressed('Esc'):
	        activate()
        # if cv2.waitKey(10) == ord('q') :
        #     break
        cv2.imshow('img',img)
        cv2.waitKey(1)


def activate():
    while(True):    
        if keyboard.is_pressed('f4'):
            print('active')
            Volume_gesture()
            break

        # elif keyboard.is_pressed('Esc'):
        #     exit()
        else:
            pass


activate()
# Volume_gesture()
        
