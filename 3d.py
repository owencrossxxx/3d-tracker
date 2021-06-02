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
tracker = Tracker(gui=True,cam_index=2)
tracker.addColorBlob("red", r=255, g=0, b=0, r_min=0, r_max=255, g_min=0, g_max=255, b_min=0, b_max=255)
tracker.addColorBlob("yellow", r=255, g=255, b=0, r_min=0, r_max=255, g_min=0, g_max=255, b_min=0, b_max=255)
# with gui disabled
# tracker = Tracker(gui=False,cam_index=2)
# tracker.addColorBlob("red", r=255, g=0, b=0, r_min=0, r_max=255, g_min=0, g_max=255, b_min=0, b_max=255)
# tracker.addColorBlob("yellow", r=255, g=255, b=0, r_min=0, r_max=255, g_min=0, g_max=255, b_min=0, b_max=255)
# tracker.setCroppingPoints(tl_x=20, tl_y=20, br_x=100, br_y=100) 
# tracker.setMorphologicalOperationParameters(dilation_size=10, erosion_size=10)

while True:
    tracker.processCamera()
    distance = tracker.getDistance("red")
    #print("distance: %3f" %distance)
    #angles = tracker.getAngles("red", "yellow")
    tracker.updateVisualizations()