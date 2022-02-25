import multiprocessing
import tkinter as tk
import cv2
import requests
import mediapipe as mp
import numpy as np
import imutils
import time

#Declaration
typeC = 0
timerDetectStart = time.time()
timerDetectEnd = timerDetectStart

#Face Detection
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

#Face Drawing
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)


e = multiprocessing.Event()
p = None

# -------begin capturing and saving video
def startrecording(e):
    cap = cv2.VideoCapture(0)

    while(cap.isOpened()):
        if e.is_set():
            cap.release()
            cv2.destroyAllWindows()
            e.clear()

def start_recording_proc():
    global p
    p = multiprocessing.Process(target=startrecording, args=(e,))
    p.start()

# -------end video capture and stop tk
def stoprecording():
    e.set()
    p.join()

    root.quit()
    root.destroy()

if __name__ == "__main__":
    # -------configure window
    root = tk.Tk()
    root.geometry("%dx%d+0+0" % (100, 100))
    startbutton=tk.Button(root,width=10,height=1,text='START',command=start_recording_proc)
    stopbutton=tk.Button(root,width=10,height=1,text='STOP', command=stoprecording)
    startbutton.pack()
    stopbutton.pack()

    # -------begin
    root.mainloop()