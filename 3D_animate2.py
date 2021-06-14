
import random
from itertools import count
from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#plt.style.use('fivethirtyeight')

ax = plt.axes(projection='3d')

namafile = 'data3D.csv'
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"

index = count()


def animate(i):
    data = pd.read_csv('data3D.csv')
    x = data[header1].to_numpy()[-5:-1]
    y = data[header2].to_numpy()[-5:-1]
    z = data[header3].to_numpy()[-5:-1]

    #print(type(x))
    plt.cla()

    ax.plot3D(x, y, z, 'red')
    ax.scatter(x, y, z, 'blue',marker='o')

    #plt.legend(loc='upper left')
    #plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()
