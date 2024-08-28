# pip install imutils
# pip install opencv-python
# pip install gradio
# pip install rpimotorlib
# pip install pathlib
import os
from imutils import paths
import cv2
from pathlib import Path
import shutil
from RpiMotorLib import RpiMotorLib
import gradio as gr

def variance_of_laplacian(image): 
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

def run():
    path = "/home/hezy/Downloads/ht/images"
    
    GPIO_pins = (14,15,18)
    direction = 20
    step = 21
    mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
    rotation = 0
    rs = 30
    while rotation < rs:
        ret, image = camera.read()
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
    for imageDir in paths.list_images(placeholderPath):
        fm = round(float(Path(imageDir).stem)*100)/100
        image = cv2.imread(imageDir)
        #blur level
        if fm < 50:
            text = "Blurry"
        else:
            text = "Not Blurry"
        # save the image
        cv2.imwrite(imagePath+"_o", image)
        cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
            cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
        print(imageDir)
        cv2.imwrite(imageDir, image)
        lst.append(fm)
        
    #type in placeholder folder directory
    print(lst)
    folder = "/home/hezy/Downloads/ht/output"
    file_name2 = str(max(lst))+".jpg_o"
    file_name = str(max(lst))+".jpg"
    print(file_name)
    new_name = os.path.join(outputPath, file_name)
    new_name2 = os.path.join(outputPath, file_name2)

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
            shutil.rmtree(filePath)
        except OSError:
           os.remove(filePath)

    dirtwo = "/home/hezy/Downloads/ht/images"
    for filestwo in os.listdir(dirtwo):
        pathtwo = os.path.join(dirtwo, filestwo)
        try:
            shutil.rmtree(filePath2)
        except OSError:
           os.remove(filePath2)
    return "images have been deleted"
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
    btn2.click(clear,outputs=[gallery])
    demo.launch(show_api=False)

