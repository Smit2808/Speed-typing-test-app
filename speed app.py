from tkinter import *
from PIL import ImageTk,Image #for image or icon
import time

# for making window 
root = Tk()
root.title("Speed Typing app")
root.iconbitmap("icon.ico")

t0 = time.time()
text_type = Entry(root,width=80, borderwidth=5)
text_type.grid(row=0,column=1,pady=10)
text_type_label = Label(root, text="Enter text to calculate speed: ")
text_type_label.grid(row=0,column=0)

def calculate():
	t1 = time.time()
	st = text_type.get()
	w_count = len(st.split())
	mylabel = Label(root, text ="TOTAL WORDS: "+str(w_count)) 
	mylabel.grid(row=2,column=0,columnspan=2)
	mylabel = Label(root, text = "TIME TAKEN: "+str(t1 -t0)) 
	mylabel.grid(row=3,column=0,columnspan=2)
	if (t1-t0) >= 10:
		mylabel = Label(root, text = "SPEED: BAD" )
		mylabel.grid(row=4,column=0,columnspan=2)
	else:
		mylabel = Label(root, text = "SPEED: GOOD" )
		mylabel.grid(row=4,column=0,columnspan=2)
 
text_type_btn = Button(root, text="calculate", command=calculate).grid(row=1,column=0,columnspan=2)


root.mainloop()