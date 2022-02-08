from tkinter import *
from processing import *

out = []

def changeValues():
    out = []
    out.append(f.get())
    out.append(minH_btn.get())
    out.append(minG_btn.get())
    out.append(minR_btn.get())
    out.append(maxH_btn.get())
    out.append(maxG_btn.get())
    out.append(maxR_btn.get())
    runImage(out)



app = Tk()

#special var for tk
f = StringVar()

#set radio btn to be empty
f.set(2)

minH_btn = Entry(app, bg='pink')
minH_txt = Label(app, text="Min Hue", bg='Black', fg='white', font=20, padx=32)
minG_btn = Entry(app, bg='pink')
minG_txt = Label(app, text="Min Saturation", bg='Black', fg='white', font=20, padx=11)
minR_btn = Entry(app, bg='pink')
minR_txt = Label(app, text="Min Value", bg='Black', fg='white', font=20, padx=25)
maxH_btn = Entry(app, bg='pink')
maxH_txt = Label(app, text="Max Hue", bg='Black', fg='white', font=20, padx=30)
maxG_btn = Entry(app, bg='pink')
maxG_txt = Label(app, text="Max Saturation", bg='Black', fg='white', font=20, padx=9)
maxR_btn = Entry(app, bg='pink')
maxR_txt = Label(app, text="Max Value", bg='Black', fg='white', font=20, padx=23)
enter_btn = Button(app, text='Change Values', bg='Blue', fg='white', command=(changeValues), padx=30, pady=30)
time_txt = Label(app, text="Press Q to end video and edit values", bg='black', fg='white', font=20, padx=40)
# For video
# vidpic = Radiobutton(app, text="Use Video", variable=v, value="vid", command=capture)
# vidpic2 = Radiobutton(app, text="Use Picture", variable=v, value="pic", command=capture)
flipbtn1 = Radiobutton(app, text="Normal Mask", variable=f, value="normal")
flipbtn2 = Radiobutton(app, text="Flip Mask", variable=f, value="flip")
minH_txt.grid(row=0, column=0)
minG_txt.grid(row=0, column=1)
minR_txt.grid(row=0, column=2)
minH_btn.grid(row=1, column=0)
minG_btn.grid(row=1, column=1)
minR_btn.grid(row=1, column=2)
maxH_txt.grid(row=2, column=0)
maxG_txt.grid(row=2, column=1)
maxR_txt.grid(row=2, column=2)
maxH_btn.grid(row=3, column=0)
maxG_btn.grid(row=3, column=1)
maxR_btn.grid(row=3, column=2)
enter_btn.grid(row=0, rowspan=4, column=4, columnspan=5)
time_txt.grid(row=5, column=0, columnspan=3)
# vidpic.grid(row=5, column=4)
# vidpic2.grid(row=5, column=5)
flipbtn1.grid(row=5, column=4)
flipbtn2.grid(row=5, column=5)
app.mainloop()