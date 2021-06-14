from numpy.core.fromnumeric import size

import time
import sys
import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import datetime
import random
import pandas as pd


from lib.tracker import Tracker

# Loop number
counter = 0
angle = 120
diameter = 28

namafile = 'data3D.csv'
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"
fieldnames = [header1, header2, header3]

with open(namafile, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

tracker1 = Tracker(gui=True,cam_index=2)
tracker1.addColorBlob("green1", r=0, g=255, b=0, r_min=70, r_max=111, g_min=130, g_max=255, b_min=112, b_max=200)
# tracker.setCroppingPoints(tl_x=20, tl_y=20, br_x=100, br_y=100) 
tracker1.setMorphologicalOperationParameters(dilation_size=6, erosion_size=2)

tracker2 = Tracker(gui=False,cam_index=0)
tracker2.addColorBlob("green2", r=0, g=255, b=0, r_min=70, r_max=145, g_min=170, g_max=255, b_min=122, b_max=255)
# tracker.setCroppingPoints(tl_x=20, tl_y=20, br_x=100, br_y=100) 
tracker2.setMorphologicalOperationParameters(dilation_size=6, erosion_size=2)


# while True:
while counter <10000:
    counter += 1
    tracker1.processCamera("green1")
    tracker1.updateVisualizations()

    tracker2.processCamera("green2")
    tracker2.updateVisualizations()

    point1 = np.asfarray(tracker1.getPoints("green1"))
    point2 = np.asfarray(tracker2.getPoints("green2"))


    if point1 == []:
        print("No marker detected by Cam1")

    if point2 == []:
        print("No marker detected by Cam2")

    # if point1.size  != point2.size:
    #     print("Not enough markers")
    #     break
    
    #print(point1,point2)
    #print(point1[:,1])

    
    if counter == 1:
        point1_original_y = np.min(point1[:,1])
        point1_original_x = point1[np.where(np.min(point1[:,1]))[0],0][0]

        point2_original_y = np.min(point2[:,1])
        point2_original_x = point2[np.where(np.min(point2[:,1]))[0],0][0]
    
    if size(point1)+size(point2) != 16:
        print("Not enough markers detected")
    else:
        point1 = point1 - [point1_original_x,point1_original_y]
        point2 = point2 - [point2_original_x,point2_original_y]
        
        x_value = point1[:,0]
        y_value = point1[:,1]
        z_value = point2[:,0]*math.cos(math.radians(angle-90))

        with open(namafile, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                header1: x_value,
                header2: y_value,
                header3: z_value
            }

            csv_writer.writerow(info)
            #print(x_value, y_value, z_value)


        #time.sleep(1)
        
    # Live 3D reconstruction

    




## Save data
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

