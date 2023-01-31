import math
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
import cv2
from imutils import paths
but1 = 1
x=0
def addition():
    global x
    x = x+1
    print(x)
def decreasation():
    global x
    x = x-1
    print(x)
def openimage():
    path =(r"C:\Users\zanyi\OneDrive\Pictures\Screenshots")
    for x in paths.list_images(path):
        img = cv2.imread(x)
        xax= int(img.shape[1] * 40 / 100)
        yax = int(img.shape[0] * 40 / 100)
        xyaxs= (xax,yax)
        resizpath=cv2.resize(img,xyaxs)
        cv2.imshow("picture",resizpath)
        cv2.waitKey()
root = tkinter.Tk()
b1 = tkinter.Button(root,text="add",command= addition)
b2 = tkinter.Button(root,text="dec",command= decreasation)
b3 = tkinter.Button(root,text="img",command= openimage)
b3.place(x=100,y=20)
b2.place(x=60,y=20)
b1.place(x=20,y=20)
root.mainloop()