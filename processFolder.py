# splits the single export folder into three different data sets for yolov5 training
# original folder is not changed

import os
import shutil
import random

#randomness to play with
random.seed(a=14)
train_percentage = 50
test_percentage = 30

# directory to folder with dataset in it
dire = "C:\\Users\\jed00\\source\\repos\\yolov5\\carPytorch\\"

# source of all data
myimages = dire + "export\\images\\"
mylabels = dire + "export\\labels\\"

# arrays for file names
pic_names = os.listdir(myimages)
label_names = os.listdir(mylabels)

# loop to copy files into appropriate folders
# you need a train, test, and valid folder in your src directory
# you need an images and label folder in each of those folders.
for i in range(pic_names.__len__()):
    r = random.randint(1, 100)
    if r > train_percentage:
        path = dire + 'train\\'
    elif r < test_percentage:
        path = dire + 'test\\'
    else:
        path = dire + 'valid\\'

    shutil.copy(myimages + pic_names[i], path + 'images')
    shutil.copy(mylabels + label_names[i], path + 'labels')

