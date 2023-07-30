import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

#1 = 3x3
#2 = 3x3
#3 = 1x1
#4 = 1x1

PST = {'111': 'Asic0_CH22',
        '112': "Asic0_CH13",
        '113': 'Asic0_CH12',
        '221': 'Asic0_CH16',
        '222': 'Asic0_CH17',
        '223': 'Asic0_CH18',
        '131': 'Asic0_CH21',
        '132': 'Asic0_CH14',
        '133': 'Asic0_CH15',
        '241': 'Asic0_CH19',
        '242': 'Asic0_CH0', 
        '243': 'Asic0_CH1',
        '151': 'Asic0_CH20',
        '152': 'Asic0_CH3',
        '153': 'Asic0_CH2',
        '261': 'Asic0_CH6',
        '262': 'Asic0_CH5',
        '263': 'Asic0_CH4',
        '171': 'Asic0_CH23',
        '172': 'Asic0_CH11',
        '173': 'Asic0_CH10',
        '281': 'Asic0_CH9',
        '282': 'Asic0_CH8',
        '283': 'Asic0_CH7'}
POST = "_HG"


fig, ax = plt.subplots()
plt.axis('off')
fig.set_size_inches(10, 7)
def draw_zire(triggerCount, data, MIN=5000, MAX=2**14, log=False):
    #define Matplotlib figure and axis
    ax.clear()
    ax.set_xlim(0, 100)
    ax.set_ylim(20, 90)
    
    event = data.iloc[triggerCount]
    colors = ['#000052','#0c44ac','#faf0ca','#ed0101','#970005'] 

    cm = LinearSegmentedColormap.from_list('custom', colors,N=100)
    cm.set_bad(color='white')
    if log:
        MAX = np.log(MAX)
        MIN = np.log(MIN)
        event = np.log(event)



    linewidth = 0.5
    edgec = 'black'

    #==============LEFT IMAGE==================================
    ax.add_patch(Rectangle((10, 80), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['111']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((20, 80), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['112']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((30, 80), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['113']+POST]  -MIN)/(MAX-MIN)*100))))

    ax.add_patch(Rectangle((10, 70), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['131']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((20, 70), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['132']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((30, 70), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['133']+POST]  -MIN)/(MAX-MIN)*100))))

    ax.add_patch(Rectangle((10, 60), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['151']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((20, 60), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['152']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((30, 60), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['153']+POST]  -MIN)/(MAX-MIN)*100))))

    ax.add_patch(Rectangle((10, 50), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['171']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((20, 50), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['172']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((30, 50), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['173']+POST]  -MIN)/(MAX-MIN)*100))))

    ax.add_patch(Rectangle((10, 30), 7.5, 5,    edgecolor=edgec, lw=linewidth))
    ax.add_patch(Rectangle((17.5, 30), 7.5, 5,  edgecolor=edgec, lw=linewidth))
    ax.add_patch(Rectangle((25, 30), 7.5, 5,    edgecolor=edgec, lw=linewidth))
    ax.add_patch(Rectangle((32.5, 30), 7.5, 5,  edgecolor=edgec, lw=linewidth))

    ax.add_patch(Rectangle((5,  45), 5, 40,     edgecolor=edgec, lw=linewidth))
    ax.add_patch(Rectangle((40, 45), 5, 40,     edgecolor=edgec, lw=linewidth))
    ax.add_patch(Rectangle((5, 25), 40, 5,      edgecolor=edgec, lw=linewidth))

    #==============RIGHT IMAGE==================================
    ax.add_patch(Rectangle((60, 75), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['221']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((70, 75), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['222']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((80, 75), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['223']+POST]  -MIN)/(MAX-MIN)*100))))

    ax.add_patch(Rectangle((60, 65), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['241']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((70, 65), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['242']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((80, 65), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['243']+POST]  -MIN)/(MAX-MIN)*100))))

    ax.add_patch(Rectangle((60, 55), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['261']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((70, 55), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['262']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((80, 55), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['263']+POST]  -MIN)/(MAX-MIN)*100))))

    ax.add_patch(Rectangle((60, 45), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['281']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((70, 45), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['282']+POST]  -MIN)/(MAX-MIN)*100))))
    ax.add_patch(Rectangle((80, 45), 10, 5, edgecolor=edgec, lw=linewidth, facecolor=cm(int((event[PST['283']+POST]  -MIN)/(MAX-MIN)*100))))

    ax.add_patch(Rectangle((50+17.5, 30), 7.5, 5,   edgecolor=edgec, lw=linewidth))
    ax.add_patch(Rectangle((50+25, 30), 7.5, 5,     edgecolor=edgec, lw=linewidth))

    ax.add_patch(Rectangle((55,  45), 5, 40,    edgecolor=edgec, lw = linewidth))
    ax.add_patch(Rectangle((90, 45), 5, 40,     edgecolor=edgec, lw = linewidth))
    ax.add_patch(Rectangle((55, 25), 40, 5,     edgecolor=edgec, lw = linewidth))
    gradient = np.linspace(0, 1, 100)
    gradient = np.vstack((gradient, gradient))
    ax.imshow(gradient, aspect='auto', cmap=cm, extent=[0, 100, 20, 21])

    plt.text(15, 87, '1')
    plt.text(25, 87, '2')
    plt.text(35, 87, '3')

    plt.text(65, 87, '1')
    plt.text(75, 87, '2')
    plt.text(85, 87, '3')

    plt.text(3, 82, '1')
    plt.text(3, 72, '3')
    plt.text(3, 62, '5')
    plt.text(3, 52, '7')

    plt.text(53, 77, '1')
    plt.text(53, 67, '3')
    plt.text(53, 57, '5')
    plt.text(53, 47, '7')

    plt.text(0, 23,  f'{MIN}')
    plt.text(96, 23, f'{MAX}')
    
    plt.axis('off')
    plt.title(f'Trigger Count {triggerCount}')

data = pd.read_csv('./data.csv')
data_np = data.to_numpy()

def animate(i):
    draw_zire(i, data)
    

ani = FuncAnimation(fig, animate, frames=2647, interval=50, repeat=False)
writervideo = animation.FFMpegWriter(fps=10)
ani.save('test.mp4', writer=writervideo)
plt.close()
