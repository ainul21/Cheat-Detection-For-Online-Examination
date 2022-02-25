import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def question ():  
    label1 = tk.Label(root, text= 'What is your Name?', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

def answer ():  
    label2 = tk.Label(root, text= 'My name is John', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label2)
    
button1 = tk.Button(text='Question',command=question, bg='brown',fg='white')
canvas1.create_window(50, 150, window=button1)

button2 = tk.Button(text='Answer',command=answer, bg='brown',fg='white')
canvas1.create_window(250, 150, window=button2)

root.mainloop()