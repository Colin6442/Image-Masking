import cv2,numpy as np
from tkinter import *
min_H = 0
min_G = 0
min_R = 0
max_B = 225
max_G = 225
max_R = 255
cap = cv2.VideoCapture(0)
img = cv2.imread(r"C:\Users\colin\PycharmProjects\Python_3\Drone Project\colorwheel.png",-1)

class App():
    def changeValues(self):
        global min_H
        min_H = self.minH_btn.get()
        global min_G
        min_G = self.minG_btn.get()
        global min_R
        min_R = self.minR_btn.get()
        global max_B
        max_B = self.maxH_btn.get()
        global max_G
        max_G = self.maxG_btn.get()
        global max_R
        max_R = self.maxR_btn.get()
        self.runImage()
    def capture(self):
        global vid_pic
        vid_pic=v.get()
        global flip
        flip=f.get()
    def runImage(self):
        while(1):
            # Take each frame
            if vid_pic=="vid":
              _,frame=cap.read()
            elif vid_pic=="pic":
              frame=img
            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # define range of blue color in HSV
            lower_blue = np.array([int(min_H),int(min_G),int(min_R)])
            upper_blue = np.array([int(max_B),int(max_G),int(max_R)])
            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            if flip=="normal":
                mask = cv2.inRange(hsv, lower_blue, upper_blue)
            elif flip=="flip":
                mask = 255-mask
            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame,frame, mask= mask)
            #blob detection
            params = cv2.SimpleBlobDetector_Params()
            params.filterByInertia = False
            params.minInertiaRatio = 0.01
            # Filter by Area.
            params.filterByArea = True
            params.minArea = 200
            params.maxArea= 100000
            # Filter by Circularity
            params.filterByCircularity = False
            params.minCircularity = 0.1
            # Filter by Convexity
            params.filterByConvexity = False
            params.minConvexity = .9
            detector = cv2.SimpleBlobDetector_create(params)
            keypoints = detector.detect(mask)
            # Draw detected blobs as red circles.
            im_with_keypoints = cv2.drawKeypoints(mask, keypoints, np.array([]), (0, 0, 255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv2.imshow('Detection',im_with_keypoints)
            cv2.imshow('Original',frame)
            cv2.imshow('Mask',mask)
            cv2.imshow('With Mask',res)
            if cv2.waitKey(20) & 0xFF == ord('q'):
              break
            #cap.realse()
            #cv2.destroyAllWinows
    def __init__(self):
        self.app=Tk()
        global v
        global f
        v=StringVar()
        v.set(2)
        f=StringVar()
        f.set(2)
        self.minH_btn=Entry(self.app,bg='pink')
        self.minH_txt=Label(self.app,text="Min Hue",bg='Black',fg='white',font=20,padx=32)
        self.minG_btn=Entry(self.app,bg='pink')
        self.minG_txt=Label(self.app,text="Min Saturation",bg='Black',fg='white',font=20,padx=11)
        self.minR_btn=Entry(self.app,bg='pink')
        self.minR_txt=Label(self.app,text="Min Value",bg='Black',fg='white',font=20,padx=25)
        self.maxH_btn=Entry(self.app,bg='pink')
        self.maxH_txt=Label(self.app,text="Max Hue",bg='Black',fg='white',font=20,padx=30)
        self.maxG_btn=Entry(self.app,bg='pink')
        self.maxG_txt=Label(self.app,text="Max Saturation",bg='Black',fg='white',font=20,padx=9)
        self.maxR_btn=Entry(self.app,bg='pink')
        self.maxR_txt=Label(self.app,text="Max Value",bg='Black',fg='white',font=20,padx=23)
        self.enter_btn=Button(self.app,text='Change Values',bg='Blue',fg='white',command=(self.changeValues),padx=30,pady=30)
        self.time_txt=Label(self.app,text="Press Q to end video and edit values",bg='black',fg='white',font=20,padx=40)
        self.vidpic=Radiobutton(self.app, text="Use Video", variable=v, value="vid",command=self.capture)
        self.vidpic2=Radiobutton(self.app, text="Use Picture", variable=v,value="pic",command=self.capture)
        self.flipbtn1=Radiobutton(self.app, text="Normal Mask", variable=f, value="normal",command=self.capture)
        self.flipbtn2=Radiobutton(self.app, text="Flip Mask", variable=f,value="flip",command=self.capture)
        self.minH_txt.grid(row=0,column=0)
        self.minG_txt.grid(row=0,column=1)
        self.minR_txt.grid(row=0,column=2)
        self.minH_btn.grid(row=1,column=0)
        self.minG_btn.grid(row=1,column=1)
        self.minR_btn.grid(row=1,column=2)
        self.maxH_txt.grid(row=2,column=0)
        self.maxG_txt.grid(row=2,column=1)
        self.maxR_txt.grid(row=2,column=2)
        self.maxH_btn.grid(row=3,column=0)
        self.maxG_btn.grid(row=3,column=1)
        self.maxR_btn.grid(row=3,column=2)
        self.enter_btn.grid(row=0,rowspan=4,column=4,columnspan=5)
        self.time_txt.grid(row=6,column=0,columnspan=3)
        self.vidpic.grid(row=5,column=4)
        self.vidpic2.grid(row=5,column=5)
        self.flipbtn1.grid(row=6,column=4)
        self.flipbtn2.grid(row=6, column=5)
        self.app.mainloop()
a=App()


#Tkinter documentation
#http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

#128,132;0,220;0,200


