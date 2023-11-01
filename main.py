from mpl_toolkits.mplot3d import Axes3D
#from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt             # plotting
import numpy as np                          # linear algebra
import os                                   # accessing directory structure
import pandas as pd                         # data processing, CSV file I/O (e.g. pd.read_csv)
from grading_cards.gradation_card_1 import *


"""for dirname, _, filenames in os.walk('C:/Users/ggh76/Desktop/recognition_of_cats_and_dogs/data/training_set'):
    for filename in filenames:
        print(os.path.join(dirname, filename))"""

root = 'C:/Users/ggh76/Desktop/recognition_of_cats_and_dogs/data/training_set/'
photo_folders = ['cats', 'dogs']

img_list = photos_in_folders_list(root, photo_folders)
print(len(img_list))


step_size = 10                                              # довжина кроку
number_of_steps = int(len(img_list) / step_size)            # кількість кроків

for i in range(number_of_steps):
    img_list, portion = random_taking_and_removing(img_list, step_size)
    print(len(img_list))
    print(i, portion, len(img_list))
    processed_portion = gradation_card_1(root, portion)
    #print(processed_portion)
    #learning_manual()
    #arr = gradation_card_1(img_list[i])
    #LM = lerning_model_1(arr, learning_manual)
    #lerning_corection = ML....
    #lerning_manual += learning_manual

#save learning_manual









