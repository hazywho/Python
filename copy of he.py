 #!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install imutils


# In[2]:


#pip install TK


# In[2]:


#pip install opencv-python


# In[3]:
import os
path ="/home/hihi/Downloads/ht/images" # shows dialog box and return the path
print(path)
os.chdir(path)
from unittest.util import sorted_list_difference 
from imutils import paths
import cv2
from tkinter import Tk
from tkinter.filedialog import askdirectory
from pathlib import Path
import shutil
import images
import RPi.GPIO as GPIO
import math
from RpiMotorLib import RpiMotorLib
import time
import math
import tkinter
from tkinter import messagebox
ifture = 0



def variance_of_laplacian(image): 
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()
    
    
    
    
    

def run():
    path ="/home/hihi/Downloads/ht/images"
    GPIO_pins = (14,15,18)
    direction = 20
    step = 21
    distance = 80 
    mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
    rotation = 0
    while rotation < 15:
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite(os.path.join(path,(str(rotation)+".jpg")), image)
        del(camera)
        mymotortest.motor_go(False, "Full", 10, 0.005, False, 0.01)
        rotation = rotation + 1 
    mymotortest.motor_go(True, "Full", 170, 0.005, False, 0.05)

    # In[4]:

     

    # loop over the input images
    for imagePath in paths.list_images(path):
        image = cv2.imread(imagePath)                      
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)

        #blur level
        if fm < 50:
            text = "Blurry"
        else:
            text = "Not Blurry"
        # show the image
        cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
            cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
        #cv2.imshow("Image", image)
        #key = cv2.waitKey(0)
        #cv2.destroyWindow 
        #typein placeholder folder directory
        defal = "/home/hihi/Downloads/ht/Placeholder"
        num=str(round(fm))+".jpg"
        cv2.imwrite(os.path.join(defal , num), image)


    list = os.listdir(defal)
    def path (x):
        fn = Path(x).stem
        return fn
    lst=[]
    for filename in list:
        lst.append(int(path(filename)))
        



    #type in output folder directory
    dst_folder = "/home/hihi/Downloads/ht/Output"



    file_name = str(max(lst))+".jpg"

    new_name = os.path.join(dst_folder, "new_base.jpg")

    shutil.move(defal + "/" + file_name, new_name )

    global ifture
    ifture = 1
    messagebox.showinfo("Add button", "Image is done capturing")
    

    

def img():
    if ifture == 1 :
    
        path ="/home/hihi/Downloads/ht/images"
        for x in paths.list_images(path):
            
            image = cv2.imread(x)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = variance_of_laplacian(gray)
                #blur level
            if fm < 50:
                text = "Blurry"
            else:
                text = "Not Blurry"
                # show the image
            cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
        
            cv2.imshow("picture",image)
            cv2.waitKey()
        dir = "/home/hihi/Downloads/ht/Placeholder"
        
        for files in os.listdir(dir):
            path = os.path.join(dir, files)
            try:
                shutil.rmtree(path)
            except OSError:
               os.remove(path)
 
        dirtwo = "/home/hihi/Downloads/ht/images"
        for filestwo in os.listdir(dirtwo):
            pathtwo = os.path.join(dirtwo, filestwo)
            try:
                shutil.rmtree(pathtwo)
            except OSError:
               os.remove(pathtwo)
        cv2.destroyAllWindows()
    else:
        return

root = tkinter.Tk()
b1 = tkinter.Button(root,text="add",command= run)
b2 = tkinter.Button(root,text="show image",command= img)
b1.place(x=20,y=20)
b2.place(x=100,y=20)
root.mainloop()


 
