import serial
import time
import sys
import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import datetime
import random

from lib.tracker import Tracker

# Loop number
counter = 0
angle = 120
diameter = 28


tracker1 = Tracker(gui=True,cam_index=0)
tracker1.addColorBlob("green1", r=0, g=255, b=0, r_min=85, r_max=110, g_min=124, g_max=255, b_min=112, b_max=160)
# tracker.setCroppingPoints(tl_x=20, tl_y=20, br_x=100, br_y=100) 
tracker1.setMorphologicalOperationParameters(dilation_size=6, erosion_size=2)

tracker2 = Tracker(gui=True,cam_index=4)
tracker2.addColorBlob("green2", r=0, g=255, b=0, r_min=100, r_max=145, g_min=170, g_max=255, b_min=122, b_max=255)
# tracker.setCroppingPoints(tl_x=20, tl_y=20, br_x=100, br_y=100) 
tracker2.setMorphologicalOperationParameters(dilation_size=6, erosion_size=2)


# while True:
while counter <10000:
    counter += 1
    tracker1.processCamera("green1")
    tracker1.updateVisualizations()
    point1 = np.asfarray(tracker1.getPoints("green1"))

    if counter == 1:
        point1_original_y = min(point1[:,1])[0]
        point1_original_x = point1[np.where(min(point1[:,1]))[0],0][0]
    

    #print (point1_original_x)
    #print(point1[0])
    #point1_x = point1[:,0]
    #point1_y = point1[:,1]
    

    #print(point)

    tracker2.processCamera("green2")
    tracker2.updateVisualizations()
    point2 = tracker2.getPoints("green2")
    #print(point2[0])


    # data processing
    

    # Live 3D reconstruction



# filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M.csv")
#     with open(filename, 'w', newline='') as f:
#         wr = csv.writer(f)
#         mylist = [x, y, z]
#         array = np.array(mylist)
#         transpose = array.T
#         mylist = transpose.tolist()
#         wr.writerows(mylist)

#     #plt.plot(x,y)
#     plt.plot(x,z)
#     plt.xlabel('time/s')
#     plt.ylabel('Length/mm')
#     plt.show()

