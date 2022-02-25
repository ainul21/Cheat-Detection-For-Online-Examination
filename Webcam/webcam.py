import cv2
import tkinter as tk

root= tk.Tk()

cap = cv2.VideoCapture(0)

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'Hello World! My Name is Meta', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
    while cap.isOpened():

        success, image = cap.read()
        cv2.imshow('Head Pose Estimation', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break


    cap.release()
    
button1 = tk.Button(text='Start',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()