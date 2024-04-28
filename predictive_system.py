# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 19:38:51 2023

@author: sania
"""

import numpy as np
import pickle

loaded_model = pickle.load(open("cc_model.sav",'rb'))



input = (0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0)
input_new = np.asarray(input)
input = input_new.reshape(1,-1)
prediction = loaded_model.predict(input)

if(prediction[0]==1):
  print("You have Anxiety mental health issues")
elif(prediction[0]==2):
  print("You have Depression mental health issues")
elif(prediction[0]==3):
  print("You have Stress mental health issues")
elif(prediction[0]==4):
  print("You have Loneliness mental health issues")
else:
  print("You are normal")
  
  