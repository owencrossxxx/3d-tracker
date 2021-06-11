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

# with gui enabled
tracker1 = Tracker(gui=True,cam_index=0)
tracker1.addColorBlob("green1", r=0, g=255, b=0, r_min=85, r_max=110, g_min=124, g_max=255, b_min=112, b_max=160)
# tracker.setCroppingPoints(tl_x=20, tl_y=20, br_x=100, br_y=100) 
tracker1.setMorphologicalOperationParameters(dilation_size=6, erosion_size=2)

tracker2 = Tracker(gui=True,cam_index=4)
tracker2.addColorBlob("green2", r=0, g=255, b=0, r_min=100, r_max=145, g_min=170, g_max=255, b_min=122, b_max=255)
# tracker.setCroppingPoints(tl_x=20, tl_y=20, br_x=100, br_y=100) 
tracker2.setMorphologicalOperationParameters(dilation_size=6, erosion_size=2)

# with gui disabled
# tracker = Tracker(gui=False,cam_index=2)
# tracker.addColorBlob("red", r=255, g=0, b=0, r_min=0, r_max=255, g_min=0, g_max=255, b_min=0, b_max=255)
# tracker.addColorBlob("yellow", r=255, g=255, b=0, r_min=0, r_max=255, g_min=0, g_max=255, b_min=0, b_max=255)
# tracker.setCroppingPoints(tl_x=20, tl_y=20, br_x=100, br_y=100) 
# tracker.setMorphologicalOperationParameters(dilation_size=10, erosion_size=10)

while True:
    
    #tracker1.processCamera("green1")
    #tracker1.updateVisualizations()
    #point1 = tracker1.getPoints("green1")
    #print(point1)

    tracker2.processCamera("green2")
    tracker2.updateVisualizations()
    point2 = tracker2.getPoints("green2")
    print(point2)