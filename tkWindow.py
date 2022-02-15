from tkinter import *
from processing import *
from time import sleep
import cv2

out = []

def changeValues(*args):
    out = []
    out.append(f.get())
    out.append(minH_btn.get())
    out.append(minS_btn.get())
    out.append(minV_btn.get())
    out.append(maxH_btn.get())
    out.append(maxS_btn.get())
    out.append(maxV_btn.get())
    out.append(name_enter.get())
    runImage(out)
    sleep(0.2)

app = Tk()

#special var for tk
f = StringVar()

#set radio btn to be empty
f.set(2)

minH_btn = Entry(app, bg='pink')
minH_txt = Label(app, text="Min Hue", bg='Black', fg='white', font=20, padx=32)
minS_btn = Entry(app, bg='pink')
minS_txt = Label(app, text="Min Saturation", bg='Black', fg='white', font=20, padx=11)
minV_btn = Entry(app, bg='pink')
minV_txt = Label(app, text="Min Value", bg='Black', fg='white', font=20, padx=25)
maxH_btn = Entry(app, bg='pink')
maxH_txt = Label(app, text="Max Hue", bg='Black', fg='white', font=20, padx=30)
maxS_btn = Entry(app, bg='pink')
maxS_txt = Label(app, text="Max Saturation", bg='Black', fg='white', font=20, padx=9)
maxV_btn = Entry(app, bg='pink')
maxV_txt = Label(app, text="Max Value", bg='Black', fg='white', font=20, padx=23)
enter_btn = Button(app, text='Change Values', bg='Blue', fg='white', command=(changeValues), padx=30, pady=30)
name_txt = Label(app, text="Enter Image Name - Ex[img.jpg]", bg='black', fg='white', font=20, padx=80)
name_enter = Entry(app, bg='pink')
# For video
# vidpic = Radiobutton(app, text="Use Video", variable=v, value="vid", command=capture)
# vidpic2 = Radiobutton(app, text="Use Picture", variable=v, value="pic", command=capture)
flipbtn1 = Radiobutton(app, text="Normal Mask", variable=f, value="normal")
flipbtn2 = Radiobutton(app, text="Flip Mask", variable=f, value="flip")

# Place text/btns
minH_txt.grid(row=0, column=0)
minS_txt.grid(row=0, column=1)
minV_txt.grid(row=0, column=2)
minH_btn.grid(row=1, column=0)
minS_btn.grid(row=1, column=1)
minV_btn.grid(row=1, column=2)
maxH_txt.grid(row=2, column=0)
maxS_txt.grid(row=2, column=1)
maxV_txt.grid(row=2, column=2)
maxH_btn.grid(row=3, column=0)
maxS_btn.grid(row=3, column=1)
maxV_btn.grid(row=3, column=2)
enter_btn.grid(row=0, rowspan=4, column=4, columnspan=5)
name_txt.grid(row=5, column=0, columnspan=3)
name_enter.grid(row=6, column=0, columnspan=3)
# vidpic.grid(row=5, column=4)
# vidpic2.grid(row=5, column=5)
flipbtn1.grid(row=5, column=4)
flipbtn2.grid(row=5, column=5)

app.bind('<Return>', changeValues)

app.mainloop()