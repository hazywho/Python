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
from ultralytics import YOLO
modelPath="/best.pt"
imagePath = "/home/hezy/Downloads/ht/images"
placeholderPath = "/home/hezy/Downloads/ht/placeholder"
outputPath = "/home/hezy/Downloads/ht/output"

def variance_of_laplacian(image): 
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

def run():
    camera = cv2.VideoCapture(0)
    GPIO_pins = (14,15,18)
    direction = 20
    step = 21
    mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
    rotation = 0
    rs = 30
    while rotation < rs:
        ret, image = camera.read()
        cv2.imwrite(os.path.join(imagePath,(str(rotation)+".jpg")), image)
        mymotortest.motor_go(1, "Half", 1, 0.005, False, 0.01)              
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        cv2.imwrite(os.path.join(placeholderPath , str(round(fm*100)/100)+".jpg"), image)
        rotation += 1
    mymotortest.motor_go(0, "Half", rs, 0.005, False, 0.01)
    
    return "images have been captured"
        
def show():
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
    file_name2 = str(max(lst))+".jpg_o"
    file_name = str(max(lst))+".jpg"
    print(file_name)
    new_name = os.path.join(outputPath, file_name)
    new_name2 = os.path.join(outputPath, file_name2)

    for filesthree in os.listdir(outputPath):
        paththree = os.path.join(outputPath, filesthree)
        try:
            shutil.rmtree(paththree)
        except OSError:
            os.remove(paththree)
    shutil.copyfile(placeholderPath + file_name, new_name )
    shutil.copyfile(placeholderPath + file_name2, new_name2 )
    storage = []
    for itemsPath in paths.list_images(placeholderPath):
        storage.append(itemsPath)
    print(storage)
    return storage
    
def delete():
    for files in os.listdir(placeholderPath):
        filePath = os.path.join(placeholderPath, files)
        try:
            shutil.rmtree(filePath)
        except OSError:
           os.remove(filePath)

    for filestwo in os.listdir(imagePath):
        filePath2 = os.path.join(imagePath, filestwo)
        try:
            shutil.rmtree(filePath2)
        except OSError:
           os.remove(filePath2)
    return "images have been deleted"

def detectAndSave():
    model = YOLO(modelPath)
    for imges in os.listdir(outputPath):
        predictImg = cv2.imread(imges)
    prediction = model.predict(source=predictImg)
    
    try:
        return f"detected cancer cell: {[prediction[0].names[val] for val in list(set(prediction[0].boxes.cls.tolist()))]}"
    except ValueError:
        return "no cancer cell detected"
#FUNCTIONS END HERE.
    
with gr.Blocks() as demo:
    out1 = gr.Textbox(value = "", label = "IMG.capture Log")
    out2 = gr.Textbox(value = "", label = "IMG.delete Log")
    out3 = gr.Textbox(value="", label= "Prediction output")
    gallery = gr.Gallery(show_label=True, elem_id = "gallery", object_fit="contain")
    btn = gr.Button(value = "Start Taking Image")
    btn.click(run,outputs=[out1])
    showb = gr.Button(value = "Show image")
    showb.click(show, outputs = [gallery])
    btn2 = gr.Button(value = "Delete")
    btn2.click(delete,outputs=out2)
    btn2.click(delete,outputs=gallery) 
    predictBtn = gr.Button(value= "Predict on current image")
    predictBtn.click(detectAndSave,outputs=out3)
    demo.launch(show_api=False)
