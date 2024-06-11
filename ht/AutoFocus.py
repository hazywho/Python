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
path ="/home/hezy/Downloads/ht/images" 
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
import gradio as gr
import re
from ultralytics import YOLO

model = YOLO("/home/hezy/Downloads/ht/best.pt")

def variance_of_laplacian(image): 
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

def recognise(path):
    img = cv2.imread(path)
    result = model.predict(img)
    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        result.show()  # display to screen
        result.save(filename="/home/hezy/Downloads/ht/output/final.jpg")  # save to disk
        
def run():
    path = "/home/hezy/Downloads/ht/images"
    
    GPIO_pins = (14,15,18)
    direction = 20
    step = 21
    distance = 80 
    mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
    rotation = 0
    rs = 30
    while rotation < rs:
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite(os.path.join(path,(str(rotation)+".jpg")), image)
        del(camera)
        mymotortest.motor_go(1, "Half", 1, 0.005, False, 0.01)
        image = cv2.imread(os.path.join(path,(str(rotation)+".jpg")))                      
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        folder = "/home/hezy/Downloads/ht/placeholder"
        num=str(round(fm*100)/100)+".jpg"
        cv2.imwrite(os.path.join(folder , num), image)
        rotation += 1
    mymotortest.motor_go(0, "Half", rs, 0.005, False, 0.01)
    
    return "images have been captured"
        
def show():
    path ="/home/hezy/Downloads/ht/placeholder"
    lst = []
        # loop over the input images
    for imagePath in paths.list_images(path):
        fm = round(float(Path(imagePath).stem)*100)/100
        image = cv2.imread(imagePath)
        #blur level
        if fm < 50:
            text = "Blurry"
        else:
            text = "Not Blurry"
        # save the image
        cv2.imwrite(imagePath+"_o", image)
        cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
            cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
        print(imagePath)
        cv2.imwrite(imagePath, image)
        
        lst.append(fm)
        
    #type in placeholder folder directory
    print(lst)
    folder = "/home/hezy/Downloads/ht/output"
    file_name2 = str(max(lst))+".jpg_o"
    file_name = str(max(lst))+".jpg"
    print(file_name)
    new_name = os.path.join(folder, file_name)
    new_name2 = os.path.join(folder, file_name2)
    
    #recognise
    recognise(new_name2)

    dirthree = "/home/hezy/Downloads/ht/output"
    for filesthree in os.listdir(dirthree):
        paththree = os.path.join(dirthree, filesthree)
        try:
            shutil.rmtree(paththree)
        except OSError:
           os.remove(paththree)
    shutil.copyfile("/home/hezy/Downloads/ht/placeholder/" + file_name, new_name )
    shutil.copyfile("/home/hezy/Downloads/ht/placeholder/" + file_name2, new_name2 )
    storage = []
    for itemsPath in paths.list_images("/home/hezy/Downloads/ht/placeholder"):
        storage.append(itemsPath)
    print(storage)
    return storage
    
def delete():
    dir = "/home/hezy/Downloads/ht/placeholder"
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
           os.remove(path)

    dirtwo = "/home/hezy/Downloads/ht/images"
    for filestwo in os.listdir(dirtwo):
        pathtwo = os.path.join(dirtwo, filestwo)
        try:
            shutil.rmtree(pathtwo)
        except OSError:
           os.remove(pathtwo)
    return "images have been deleted"

def clear():
    return None

#FUNCTIONS END HERE.
    
with gr.Blocks() as demo:
    out1 = gr.Textbox(value = "", label = "IMG.capture Log")
    out2 = gr.Textbox(value = "", label = "IMG.delete Log")
    gallery = gr.Gallery(show_label=True, elem_id = "gallery", object_fit="contain")
    btn = gr.Button(value = "Start Taking Image")
    btn.click(run,outputs=[out1])
    showb = gr.Button(value = "Show image")
    showb.click(show, outputs = [gallery])
    btn2 = gr.Button(value = "Delete")
    btn2.click(delete,outputs=out2)
    btn2.click(delete,outputs=gallery) 
    demo.launch(show_api=False, share=True)
