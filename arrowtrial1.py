import cv2
import math
import numpy as np
import freenect
#video=cv2.VideoCapture(0)
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
def dist(a,b,c,d):
    d1=math.sqrt((a-c)**2+(b-d)**2)
    return d1
while True:
    #_,frame=video.read()
    #l_arrw=np.array([20,92,7])
    #u_arrw=np.array([64,255,255])
    #ball
    #l_arrw=np.array([58,65,0])
    #u_arrw=np.array([162,255,89])
    #blue arrw
    frame=get_video()
    l_arrw=np.array([58,65,0])
    u_arrw=np.array([162,255,89])
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,l_arrw,u_arrw)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    canny=cv2.Canny(mask,100,200)
    contours=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[-2]
    #cv2.drawContours(frame,contours,-1,(0,0,255),3)
    for cnt in contours:
          area=cv2.contourArea(cnt)       
          approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
          x=approx.ravel()[0]
          y=approx.ravel()[1]
          if area>400:
             left=tuple(cnt[cnt[:,:,0].argmin()][0])
             right=tuple(cnt[cnt[:,:,0].argmax()][0])
             top=tuple(cnt[cnt[:,:,1].argmin()][0])
             bottom=tuple(cnt[cnt[:,:,1].argmax()][0])
             cv2.circle(frame,left,8,(0,255,0),3)
             cv2.circle(frame,right,8,(0,0,255),3)
             cv2.circle(frame,top,8,(255,255,255),3)
             cv2.circle(frame,bottom,8,(255,0,0),3)
             print(left)
             print(right)
             (a,b)=top
             (x1,y1)=left
             (x2,y2)=right
             (c,d)=bottom
             cr=0
             cl=0
             cs=0
             if len(approx)>7:
                 detected=True
                 cv2.drawContours(frame,[approx],0,(0,0,0),5)
                 cv2.putText(frame,"arrw",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
                 for n in range(0,10):
                    if(dist(x1,y1,x2,y2)>dist(a,b,c,d)):
                     if(dist(a,b,x1,y1)<dist(a,b,x2,y2)):
                         #print("right side arrow fgoooooo righhtt")
                         cr=cr+1 
                     else:
                        #print("goo left")
                        cl=cl+1
                    else:
                       cs=cs+1
                     #print("goo stttttttrght")
                 if(cr>cl and cr>cs):
                     print("leeeftttt")
                 elif(cl>cr and cl>cs):
                     print("riiiiiiiggghhhhhhttttttt")
                 else:
                     print("strrght")

                     
                     
                 """if(int(dist(x1,y1,x2,y2))in range(170,190)):
                     if(dist(a,b,x1,y1)<dist(a,b,x2,y2)):
                         print("right side arrow fgoooooo righhtt")
                          
                     else:
                        print("goo left")
                       
                 else:
                        print("goo strght")
             break """          
    #corners=cv2.goodFeaturesToTrack(mask,7,0.8,50)
    #corners=np.int0(corners)
    #for corner in corners:
    #    x,y=corner.ravel()
    #    cv2.circle(frame,(x,y),3,(0,255,0),-1)
    #c=max(contours,key=cv2.contourArea)
    """for c in contours:
        extleft=tuple(c[c[:, :, 0].argmin()][0])
        extright=tuple(c[c[:, :, 0].argmax()][0])              
        exttop=tuple(c[c[:, :, 1].argmin()][0])
        extbottom=tuple(c[c[:, :, 1].argmax()][0])
        cv2.drawContours(frame,[c],0,(0,255,23),2)
        cv2.circle(frame,extleft,8,(0,255,4),3)
        cv2.circle(frame,extright,8,(244,0,234),3)
        cv2.circle(frame,exttop,8,(0,0,234),3)
        cv2.circle(frame,extbottom,8,(0,0,4),3)
        print(extleft)
        print(extright)
        print(exttop)
        print(extbottom)"""
        
    cv2.imshow("frame",frame)
    cv2.imshow("Mask",mask)
    
    key=cv2.waitKey(1)
    if key==27:
        break
#frame.release()
cv2.destroyAllWindows()
       
