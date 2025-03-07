# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U8fL62AdRto8ByZyUozAGVKnorFQyYMW
"""

import cv2
from tensorflow.keras.models import Sequential, model_from_json
import os
import numpy as np
import sys

file=open("model.json",'r')
modelj=file.read()
model=model_from_json(modelj)
file.close
model.load_weights('model.h5')

image_path=sys.argv[1]
image=cv2.imread(image_path)
image=cv2.resize(image,(150,150))
img_arr=np.array(image)
img_arr=img_arr.reshape(1,150,150,3)
img_arr.shape

result=model.predict(img_arr)
index=result.argmax()

if index==0:
  print("Glioma_tumor")
elif index==1:
  print("Meningioma_tumor")
elif index==2:
  print("No Tumor")
elif index==3:
  print("Pituitary_tumor")