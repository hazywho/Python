#Code & logic by Ong Chong Yao
#fully functional as of 24/6/2024
# :D good luck!

#Python 3.11, Nvidia Cuda 12.1

#Do the following based on this order:
#1) Nvidia Cuda 12.1 download page: https://developer.nvidia.com/cuda-12-1-0-download-archive
#2) pip install firebase_admin==6.5.0 certifi==2022.12.7 charset-normalizer==2.1.1 colorama==0.4.6 contourpy==1.2.0 cycler==0.12.1 filelock==3.9.0 fonttools==4.47.0 fsspec==2023.4.0 idna==3.4 Jinja2==3.1.2 kiwisolver==1.4.5 labelImg==1.8.6 lxml==5.0.0 MarkupSafe==2.1.3 matplotlib==3.8.2 mpmath==1.3.0 networkx==3.0 numpy==1.24.1 opencv-python==4.9.0.80 packaging==23.2 pandas==2.1.4 Pillow==9.3.0 pip==23.3.2 psutil==5.9.7 py-cpuinfo==9.0.0 pyparsing==3.1.1 PyQt5==5.15.10 PyQt5-Qt5==5.15.2 PyQt5-sip==12.13.0 python-dateutil==2.8.2 pytz==2023.3.post1 PyYAML==6.0.1 requests==2.28.1 scipy==1.11.4 seaborn==0.13.1 setuptools==65.5.0 six==1.16.0 sympy==1.12 thop==0.1.1.post2209072238 tqdm==4.66.1 typing_extensions==4.4.0 tzdata==2023.4 ultralytics==8.0.231 urllib3==1.26.13
#3) pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

#in case that your computer does not have Nvidia Cuda-enabled GPU, the code will then run on CPU
#the Firebase credentials have to be downloaded from Firebase if the database info changes

import cv2
import pandas as pd

import torch
from ultralytics import YOLO
import math
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "sis-ai-item-tracker-358e4",
  "private_key_id": "fd767e840d07e060111a4984b77d33d3487ded14",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC2RuEY0kQJETAK\n+bAL9RvZMYFvyn328K6k/lKm1q3DLDpqMHRH+Aanw9Usj4gVU7iwgVkgfF3ntVsf\nkeQvtVsDTt2/1h4VAm77oTvNBT/hbIs76jHIvDC//TKVnm7RI9ASw+Hg5aOk8RE6\nFbhQjbiricBRMax9BK9/JNjxwQ3E+4ZjDWqZkQQDXqumzxPGV0nS/V++HiTwHOtY\nq5U0+yTg1fklCYN+SE48xuu7Htge20XGLXlv1rsg6OAwQo+4MmtnRYRpWo2vSG7f\nh21z82+1HRNlXUniZrLTS/ZJd8Ppyfa0Qr6t0vyWweur+gOPhtoB0RvTEqEaUCdp\nAxLt44ShAgMBAAECggEALRXUlRljMzPxZHGUmiyPLhaI69AT/qnTJOP0KSjGE5XD\nwCLKjEecy8/MUWiSMiZCc0QXOcoRRyAMUT96h9NtluChyFLLn4o5zds4abJ/9b/t\no4z+seZcj4xu/+OPiQL48z9IxmI+qyxmhK29KI2ZbTKWI28sOUMYrpP8ZjXIdF2Q\nnS5Y8GT4SKy2XQnFMzIWJFgr+5Gj7EJQl3gsCD/N99AJWVkMBPsXP9CoEQ+JingY\noz+yfhOax3PzMJl+HyMctb1am9oKbdUE/Lg/mhtrfB4dgHWY37VxqFwkYUI2ASss\n8+NQMCuPQ7iDfWuiqj6/RpMlxG2FGDavF3ckkuxDDQKBgQDeJ8lHDnalp50E1Vuf\nfYFYO7ToiA8TUMbzxZREJHapRZfn3tSdOsfhKnkl8aYqeUMiukxLQv1wU3S4qEgZ\nKz41PnRLT72SZn7b20zHPYCvE4AdmvAMqSoSGLl5hTusrba3pt5g/PQKFpchgTNo\nXN7lygmwtXtmKIgviLWH6+KNjQKBgQDSC81vzizSvyeENoBBFPb56yrxwcnr7mmy\nvRM9/xDBjq3xWgEQEOCMGu6SzzTVDIoRbKiUjK8UyJH67rOcT/OqSa4vlfX3vq/b\n7TY35Yj/qJJzyS95NNt3fGN4KSCipQh4T5YCKHCRGJuHZMKFxPV+pU0PkL61B0k8\nmUbHfO9cZQKBgGRXMhlPFhXyZACH4c9i36YbqbWRpsWBqar3ZeV1VsdT8K3BPuUZ\nZKh2B6w0vmnWxZUM8mLYCiLO/xxcndwIZRulbt+JT8WtV8U0AzTGubXaJ/a3QY9m\nZOMxmayimfZ/q9S9oRnLhup7k52FftO3htHhdIkFH4xf6EsYA242A+kNAoGBAL+c\nZq9MzNT/7kONGFjGkDsSjd125AXnOuMD2q7epOF9kC4w5fFLBByrYOHqRg7oXndg\nwTSqVflGsuzPnmfFA8pfZpggW/7CJFkjPyekq+JVXCxl5nnSfzaz8WWnVw8oL97Y\n80ZKr82dPhw4Db/MGguLLg46A87Os7+lL81BqnWFAoGBAIBQdM3ti0qxdFVmubdc\nLjgCRwIoTMOcrTznY8tc+5j69PI/gxje0XC7lmBMzmJplsK7NN6QJ3M1g90zZFT2\nHz+wYVaJ+bS0b9qLJtyeUzWLHQkzflYUbA+por4GL06PjnQB/9WzAbliJYuG1VC3\nsUuhtuPqBsj1OaQQcedcEfNp\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-814b2@sis-ai-item-tracker-358e4.iam.gserviceaccount.com",
  "client_id": "112296305151074226600",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1  /certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-814b2%40sis-ai-item-tracker-358e4.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sis-ai-item-tracker-358e4-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

root_ref = db.reference()

class Tracker:
    def __init__(self):
        self.center_points = {}
        self.id_count = 0
        self.id_to_class = {}
        self.id_to_confidence = {}

    def update(self, objects_rect, class_names, confidences):
        objects_bbs_ids = []
        for rect, class_name, confidence in zip(objects_rect, class_names, confidences):
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])
                if dist < 50:
                    if confidence > self.id_to_confidence.get(id, 0):
                        self.center_points[id] = (cx, cy)
                        self.id_to_class[id] = class_name
                        self.id_to_confidence[id] = confidence
                    objects_bbs_ids.append([x, y, w, h, id, class_name])
                    same_object_detected = True
                    break
            if not same_object_detected:
                self.center_points[self.id_count] = (cx, cy)
                self.id_to_class[self.id_count] = class_name
                self.id_to_confidence[self.id_count] = confidence
                objects_bbs_ids.append([x, y, w, h, self.id_count, class_name])
                self.id_count += 1
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id, _ = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center
        self.center_points = new_center_points.copy()
        return objects_bbs_ids

# Check if CUDA is available and set PyTorch device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = YOLO('yolo11n.pt')
# nsmlx small to big
model.to('cuda')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        #print(colorsBGR)

def wrap_text(text, max_width, font, font_scale, thickness):
    words = text.split(' ')
    lines = []
    current_line = words[0]

    for word in words[1:]:
        if cv2.getTextSize(current_line + ' ' + word, font, font_scale, thickness)[0][0] <= max_width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture(1)

class_list = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

print(class_list)

frame_count = 0

tracker = Tracker()

cy1 = 200
cy2 = 320
offset = 60

vh_down = {}
vh_up = {}
incounter = {}
outcounter = {}
objects_inside_names = []

while True:
    ret, frame = cap.read()
    frame_count += 1
    frame = cv2.resize(frame, (800, 500))

    results = model.predict(frame, show=True)
    a = results[0].boxes.data
    px = pd.DataFrame(a.cpu()).astype("float")
    bbox_list = []
    class_names = []
    confidences = []

    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        confidence = float(row[4])
        d = int(row[5])
        c = class_list[d]
        if c == 'person':
            continue
        bbox_list.append([x1, y1, x2, y2])
        class_names.append(c)
        confidences.append(confidence)

    bbox_id = tracker.update(bbox_list, class_names, confidences)

    for bbox in bbox_id:
        x3, y3, x4, y4, id, class_name = bbox
        cx = int(x3 + x4) // 2
        cy = int(y3 + y4) // 2
        print(f"Tracking ID: {id}, Class: {class_name}, Coordinates: ({cx}, {cy})")  # Debugging statement
        if cy1 < (cy + offset) and cy1 > (cy - offset):  # going in
            vh_down[id] = (cy, class_name, False)  # Add a flag for counting
        if id in vh_down:
            if cy2 < (cy + offset) and cy2 > (cy - offset) and not vh_down[id][2]:
                cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
                cv2.putText(frame, f"{id} ({class_name})", (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
                incounter[id] = class_name
                objects_inside_names.append(class_name)
                vh_down[id] = (cy, class_name, True)  # Update the flag to True

        if cy2 < (cy + offset) and cy2 > (cy - offset):  # going out
            vh_up[id] = (cy, class_name, False)  # Add a flag for counting
        if id in vh_up:
            if cy1 < (cy + offset) and cy1 > (cy - offset) and not vh_up[id][2]:
                cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
                cv2.putText(frame, f"{id} ({class_name})", (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
                outcounter[id] = class_name
                if class_name in objects_inside_names:
                    objects_inside_names.remove(class_name)
                vh_up[id] = (cy, class_name, True)  # Update the flag to True

    cv2.line(frame, (0, cy1), (800, cy1), (255, 255, 255), 1)
    cv2.line(frame, (0, cy2), (800, cy2), (255, 255, 255), 1)
    cv2.putText(frame, f"going in: {list(incounter.items())}", (60, 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
    cv2.putText(frame, f"going out: {list(outcounter.items())}", (60, 130), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
    cv2.putText(frame, f"Objects inside: {objects_inside_names}", (60, 360), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
    cv2.putText(frame, f"Number of objects inside: {len(incounter) - len(outcounter)}", (60, 450), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
    cv2.imshow("RGB", frame)
    if frame_count % 30 == 0:
        data_ref = root_ref.child('Data')
        data = {
            'going in': str(list(incounter.items())),
            'going out': str(list(outcounter.items())),
            'Number of objects inside': str(len(incounter) - len(outcounter)),
            'Objects inside': str(objects_inside_names)
        }
        data_ref.set(data)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()