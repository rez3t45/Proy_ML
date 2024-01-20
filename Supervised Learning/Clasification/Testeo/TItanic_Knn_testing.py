# Cargar nuestro modelo del disco duro 
import pickle 
import pandas as pd 
import numpy as np 

#Ubicarme en la rais para poder utilizar todas las carpetas
from sys import path
import os

#path.append(os.path.realpath('../'))

#'../../datasets/Titanic_train.csv'

# Cargamos nuestro modelo en memoria
pkl_filename = "Titanic_Knn_Predict_Survival.pkl"
with open(pkl_filename, 'rb') as file :
    pickle_model = pickle.load(file)