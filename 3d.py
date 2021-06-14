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
from itertools import zip_longest


from lib.tracker import Tracker

# Loop number
counter = 0
angle = 120
diameter = 28

x_value = []
y_value = []
z_value = []

namafile = 'data3D.csv'
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"
fieldnames = [header1, header2, header3]

with open(namafile, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

# with gui enabled
tracker1 = Tracker(gui=True,cam_index=2)
tracker1.addColorBlob("green1", r=0, g=255, b=0, r_min=0, r_max=65, g_min=72, g_max=255, b_min=50, b_max=110)
# tracker.setCroppingPoints(tl_x=20, tl_y=20, br_x=100, br_y=100) 
tracker1.setMorphologicalOperationParameters(dilation_size=6, erosion_size=2)

tracker2 = Tracker(gui=False,cam_index=0)
tracker2.addColorBlob("green2", r=0, g=255, b=0, r_min=0, r_max=67, g_min=86, g_max=255, b_min=84, b_max=175)
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
        #point1_original_x = point1[np.where(np.min(point1[:,1]))[0],0][0]
        point1_original_x = point1[:,0]

        point2_original_y = np.min(point2[:,1])
        #point2_original_x = point2[np.where(np.min(point2[:,1]))[0],0][0]
        point2_original_x = point2[:,0]
    
    if size(point1)+size(point2) > 2*size(point1):
        print("Too many markers detected")
        continue
    if size(point1)+size(point2) < 2*size(point1):
        print("Not enough markers detected")
        continue
    else:
        point1 = point1 - [0,point1_original_y]
        point2 = point2 - [0,point2_original_y]

        point1[:,0] = point1[:,0] - point1_original_x
        point2[:,0] = point2[:,0] - point2_original_x
        
        x_value = x_value+point1[:,0].tolist()
        y_value = y_value+point1[:,1].tolist()
        z_value = z_value+(point2[:,0]*math.cos(math.radians(angle-90))).tolist()

        #Threshold


        #print(point1[:,0].tolist())
        #print(x_value)
        
        rows = [x_value,y_value,z_value]

        export_data = zip_longest(*rows, fillvalue = '')
        with open(namafile, 'w', encoding="ISO-8859-1", newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerow(("x", "y","z"))
            wr.writerows(export_data)
        #myfile.close()


        

        # with open(namafile, 'a') as csv_file:
        #     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        #     info = {
        #         header1: x_value,
        #         header2: y_value,
        #         header3: z_value
        #     }

        #     csv_writer.writerow(info)
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

