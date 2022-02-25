from tkinter import *
from PIL import ImageTk, Image  
import os

def next_frame(nframe):
    nframe.tkraise()

def run_CDS():
    os.system('python cheatDetection.py')

root = Tk()
root.state('zoomed')
root.title("Welcome to Cheat Detection System For Online Examination")
root.geometry("1350x700+0+0")

main_frame = Frame(root, bg="#111183")
cds_frame = Frame(root)

for frame in (main_frame, cds_frame):
    frame.place(x=0,y=0, relheigh=1, relwidth=1)

main_frame.tkraise()

#Cheat Detection System
cds_frame.configure(bg="#111183")
inframe = Frame(cds_frame)
inframe.place(x=250, y=100, height = 500, width=800)
Label3 = Label(inframe, text = "In this project,\nWe are using Opencv with \n Mediapipe Library.\nMake sure that:\n\n1.Camera shutter is open\n2.Try to position yourself \n at the center of the camera\n3.Press Q to exit the Program.", justify=LEFT, font=("Times", 15))
Label3.place(x=0.1, y=0.1, height=400, width = 370)
Label1 = Label(inframe, text = "Cheat Detection System", relief=SUNKEN, justify=CENTER, font=("Arial Bold", 23))
Label1.place(x=25, y=25, height=50, width=350)
Label2 = Label(inframe, relief=SUNKEN)
Label2.place(x=400, y=10, height=400, width=415)


img1 = Image.open('Images\\cds_picture.png')
img2 = img1.resize((400,200), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img2)
Bottom_label = Label(inframe, image = img3)
Bottom_label.place(x =410,y = 100, height= 200, width = 400)
Status_label = Label(inframe, relief=SUNKEN)
Status_label.place(x=15, y= 420, height = 90, width = 800)
status_Button = Button(inframe, text = "Run Project", command = run_CDS)
status_Button.place(height = 70, width = 200,  x=400, y = 425)
back_Button = Button(inframe, text = "Back", command = lambda: next_frame(main_frame))
back_Button.place(height = 70, width = 200,  x=100, y = 425)

# ---------END OF SUB FRAMES---------

mfimg3 = ImageTk.PhotoImage(Image.open('Images\\main_picture(s).png'))
Bgimglabel = Label(main_frame, image = mfimg3)
Bgimglabel.place(x =0,y =0, relwidth = 1, relheight = 1)

#TitleHead = Label(main_frame, text="SKEM4133", font=("Times", 100), bg = '#111183',fg = '#ffffff')
#TitleHead.place(x = 200, y=50)

ButtonCDS = Button(main_frame, text="Cheat Detection System", command = lambda: next_frame(cds_frame))
ButtonCDS.place(y = 350, x = 650)

root.mainloop()