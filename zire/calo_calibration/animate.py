import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import matplotlib as mpl


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

CALOG = {   '16': 'Asic2_CH2',
            '13': 'Asic2_CH3',
            '11': 'Asic2_CH4',
            '26': 'Asic2_CH5',
            '23': 'Asic2_CH6',
            '21': 'Asic2_CH7',
            '36': 'Asic2_CH8',
            '33': 'Asic2_CH9',
            '31': 'Asic2_CH10',
            '46': 'Asic2_CH11',
            '43': 'Asic2_CH12',
            '41': 'Asic2_CH13',
            '56': 'Asic2_CH14',
            '53': 'Asic2_CH15',
            '51': 'Asic2_CH16',
            '66': 'Asic2_CH17',
            '63': 'Asic2_CH18',
            '61': 'Asic2_CH19',
            '76': 'Asic2_CH20',
            '73': 'Asic2_CH21',
            '71': 'Asic2_CH22',
            '86': 'Asic2_CH23',
            '83': 'Asic2_CH24',
            '81': 'Asic2_CH25'}

POST = "_LG"
print("LOADING DATA")
#Importing the data
data_path = './run_71/data.csv'
data_71 = pd.read_csv(data_path)

data_path = './run_73/data.csv'
data_73 = pd.read_csv(data_path)

data_path = './run_66/data.csv'
data_66 = pd.read_csv(data_path)
print('DATA LOADED')
fig, ax = plt.subplots()
fig.set_size_inches(9.5, 5)

def draw_zire_calo(triggerCount, data1, data2, data3):
    ax.clear()
    ax.set_xlim(0, 95)
    ax.set_ylim(0, 50)
    #define Matplotlib figure and axis
    event_1 = data1.iloc[triggerCount]
    event_2 = data2.iloc[triggerCount]
    event_3 = data3.iloc[triggerCount]
    #colors = ['#000052','#0c44ac','#faf0ca','#ed0101','#970005'] 
    #colors = ['#000000', '#ffffff'] 

    #cm = LinearSegmentedColormap.from_list('custom', colors,N=100)
    cm = mpl.colormaps['viridis']
    cm.set_bad(color='white')
    
    linewidth = 0.5
    edgec = 'black'
    
    # Fisrt box
    
    MIN2 = np.min([event_1[CALOG[i+'6']+POST] + event_1[CALOG[i+'3']+POST] + event_1[CALOG[i+'1']+POST] for i in [str(i) for i in range(1, 9)]])
    MAX2 = np.max([event_1[CALOG[i+'6']+POST] + event_1[CALOG[i+'3']+POST] + event_1[CALOG[i+'1']+POST] for i in [str(i) for i in range(1, 9)]]) + 1

    ax.add_patch(Rectangle((10,     32.5), 7.5, 7.5,                edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_1[CALOG['13']+POST]+event_1[CALOG['16']+POST] + event_1[CALOG['11']+POST] - MIN2)/(MAX2-MIN2)*256  ))))
    ax.add_patch(Rectangle((17.5,   32.5), 7.5, 7.5,                edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_1[CALOG['23']+POST]+event_1[CALOG['26']+POST] + event_1[CALOG['21']+POST] - MIN2)/(MAX2-MIN2)*256  ))))
    ax.add_patch(Rectangle((10,     32.5-7.5), 7.5, 7.5,            edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_1[CALOG['33']+POST]+event_1[CALOG['36']+POST] + event_1[CALOG['31']+POST] - MIN2)/(MAX2-MIN2)*256  ))))
    ax.add_patch(Rectangle((17.5,   32.5-7.5), 7.5, 7.5,            edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_1[CALOG['43']+POST]+event_1[CALOG['46']+POST] + event_1[CALOG['41']+POST] - MIN2)/(MAX2-MIN2)*256  ))))
    ax.add_patch(Rectangle((10,     32.5-7.5-7.5), 7.5, 7.5,        edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_1[CALOG['53']+POST]+event_1[CALOG['56']+POST] + event_1[CALOG['51']+POST] - MIN2)/(MAX2-MIN2)*256  ))))
    ax.add_patch(Rectangle((17.5,   32.5-7.5-7.5), 7.5, 7.5,        edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_1[CALOG['63']+POST]+event_1[CALOG['66']+POST] + event_1[CALOG['61']+POST] - MIN2)/(MAX2-MIN2)*256  ))))
    ax.add_patch(Rectangle((10,     32.5-7.5-7.5-7.5), 7.5, 7.5,    edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_1[CALOG['73']+POST]+event_1[CALOG['76']+POST] + event_1[CALOG['71']+POST] - MIN2)/(MAX2-MIN2)*256  ))))
    ax.add_patch(Rectangle((17.5,   32.5-7.5-7.5-7.5), 7.5, 7.5,    edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_1[CALOG['83']+POST]+event_1[CALOG['86']+POST] + event_1[CALOG['81']+POST] - MIN2)/(MAX2-MIN2)*256  ))))

    gradient = np.linspace(0, 1, 100)
    gradient = np.vstack((gradient, gradient))
    plt.imshow(gradient, aspect='auto', cmap='viridis', extent=[10, 25, 1, 2])

    MIN3 = np.min([event_2[CALOG[i+'6']+POST] + event_2[CALOG[i+'3']+POST] + event_2[CALOG[i+'1']+POST] for i in [str(i) for i in range(1, 9)]])
    MAX3 = np.max([event_2[CALOG[i+'6']+POST] + event_2[CALOG[i+'3']+POST] + event_2[CALOG[i+'1']+POST] for i in [str(i) for i in range(1, 9)]]) + 1

    ax.add_patch(Rectangle((30+10,     32.5), 7.5, 7.5,                edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_2[CALOG['13']+POST]+event_2[CALOG['16']+POST] + event_2[CALOG['11']+POST] - MIN3)/(MAX3-MIN3)*256  ))))
    ax.add_patch(Rectangle((30+17.5,   32.5), 7.5, 7.5,                edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_2[CALOG['23']+POST]+event_2[CALOG['26']+POST] + event_2[CALOG['21']+POST] - MIN3)/(MAX3-MIN3)*256  ))))
    ax.add_patch(Rectangle((30+10,     32.5-7.5), 7.5, 7.5,            edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_2[CALOG['33']+POST]+event_2[CALOG['36']+POST] + event_2[CALOG['31']+POST] - MIN3)/(MAX3-MIN3)*256  ))))
    ax.add_patch(Rectangle((30+17.5,   32.5-7.5), 7.5, 7.5,            edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_2[CALOG['43']+POST]+event_2[CALOG['46']+POST] + event_2[CALOG['41']+POST] - MIN3)/(MAX3-MIN3)*256  ))))
    ax.add_patch(Rectangle((30+10,     32.5-7.5-7.5), 7.5, 7.5,        edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_2[CALOG['53']+POST]+event_2[CALOG['56']+POST] + event_2[CALOG['51']+POST] - MIN3)/(MAX3-MIN3)*256  ))))
    ax.add_patch(Rectangle((30+17.5,   32.5-7.5-7.5), 7.5, 7.5,        edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_2[CALOG['63']+POST]+event_2[CALOG['66']+POST] + event_2[CALOG['61']+POST] - MIN3)/(MAX3-MIN3)*256  ))))
    ax.add_patch(Rectangle((30+10,     32.5-7.5-7.5-7.5), 7.5, 7.5,    edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_2[CALOG['73']+POST]+event_2[CALOG['76']+POST] + event_2[CALOG['71']+POST] - MIN3)/(MAX3-MIN3)*256  ))))
    ax.add_patch(Rectangle((30+17.5,   32.5-7.5-7.5-7.5), 7.5, 7.5,    edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_2[CALOG['83']+POST]+event_2[CALOG['86']+POST] + event_2[CALOG['81']+POST] - MIN3)/(MAX3-MIN3)*256  ))))

    plt.imshow(gradient, aspect='auto', cmap='viridis', extent=[30+10, 30+25, 1, 2])

    MIN4 = np.min([event_3[CALOG[i+'6']+POST] + event_3[CALOG[i+'3']+POST] + event_3[CALOG[i+'1']+POST] for i in [str(i) for i in range(1, 9)]])
    MAX4 = np.max([event_3[CALOG[i+'6']+POST] + event_3[CALOG[i+'3']+POST] + event_3[CALOG[i+'1']+POST] for i in [str(i) for i in range(1, 9)]]) + 1

    ax.add_patch(Rectangle((60+10,     32.5), 7.5, 7.5,                edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_3[CALOG['13']+POST]+event_3[CALOG['16']+POST] + event_3[CALOG['11']+POST] - MIN4)/(MAX4-MIN4)*256  ))))
    ax.add_patch(Rectangle((60+17.5,   32.5), 7.5, 7.5,                edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_3[CALOG['23']+POST]+event_3[CALOG['26']+POST] + event_3[CALOG['21']+POST] - MIN4)/(MAX4-MIN4)*256  ))))
    ax.add_patch(Rectangle((60+10,     32.5-7.5), 7.5, 7.5,            edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_3[CALOG['33']+POST]+event_3[CALOG['36']+POST] + event_3[CALOG['31']+POST] - MIN4)/(MAX4-MIN4)*256  ))))
    ax.add_patch(Rectangle((60+17.5,   32.5-7.5), 7.5, 7.5,            edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_3[CALOG['43']+POST]+event_3[CALOG['46']+POST] + event_3[CALOG['41']+POST] - MIN4)/(MAX4-MIN4)*256  ))))
    ax.add_patch(Rectangle((60+10,     32.5-7.5-7.5), 7.5, 7.5,        edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_3[CALOG['53']+POST]+event_3[CALOG['56']+POST] + event_3[CALOG['51']+POST] - MIN4)/(MAX4-MIN4)*256  ))))
    ax.add_patch(Rectangle((60+17.5,   32.5-7.5-7.5), 7.5, 7.5,        edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_3[CALOG['63']+POST]+event_3[CALOG['66']+POST] + event_3[CALOG['61']+POST] - MIN4)/(MAX4-MIN4)*256  ))))
    ax.add_patch(Rectangle((60+10,     32.5-7.5-7.5-7.5), 7.5, 7.5,    edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_3[CALOG['73']+POST]+event_3[CALOG['76']+POST] + event_3[CALOG['71']+POST] - MIN4)/(MAX4-MIN4)*256  ))))
    ax.add_patch(Rectangle((60+17.5,   32.5-7.5-7.5-7.5), 7.5, 7.5,    edgecolor=edgec, lw=linewidth, facecolor=cm(int(  (event_3[CALOG['83']+POST]+event_3[CALOG['86']+POST] + event_3[CALOG['81']+POST] - MIN4)/(MAX4-MIN4)*256  ))))

    plt.imshow(gradient, aspect='auto', cmap='viridis', extent=[60+10, 60+25, 1, 2])

    plt.text(10, 3, f'{MIN2}')
    plt.text(25, 3, f'{MAX2}')

    plt.text(30+10, 3, f'{MIN3}')
    plt.text(30+25, 3, f'{MAX3}')

    plt.text(60+10, 3, f'{MIN4}')
    plt.text(60+25, 3, f'{MAX4}')

    plt.text(15, 42, "Run 71")
    plt.text(30+15, 42, "Run 73")
    plt.text(60+15, 42, "Run 66")

    plt.text(7,     36, '1')
    plt.text(28,    36, '2')
    plt.text(7,     36-7.5, '3')
    plt.text(28,    36-7.5, '4')
    plt.text(7,     36-15, '5')
    plt.text(28,    36-15, '6')
    plt.text(7,     36-15-7.5, '7')
    plt.text(28,    36-15-7.5, '8')
   
    plt.text(30+7,     36, '1')
    plt.text(30+28,    36, '2')
    plt.text(30+7,     36-7.5, '3')
    plt.text(30+28,    36-7.5, '4')
    plt.text(30+7,     36-15, '5')
    plt.text(30+28,    36-15, '6')
    plt.text(30+7,     36-15-7.5, '7')
    plt.text(30+28,    36-15-7.5, '8')

    plt.text(60+7,     36, '1')
    plt.text(60+28,    36, '2')
    plt.text(60+7,     36-7.5, '3')
    plt.text(60+28,    36-7.5, '4')
    plt.text(60+7,     36-15, '5')
    plt.text(60+28,    36-15, '6')
    plt.text(60+7,     36-15-7.5, '7')
    plt.text(60+28,    36-15-7.5, '8')

    plt.title(f'Trigger Count: {triggerCount}')
    plt.axis('off')
    #plt.show()


def animate(i):
    draw_zire_calo(i, data_71, data_73, data_66)
    
print('CREATING ANIMATION')
ani = FuncAnimation(fig, animate, frames=1000, interval=2000, repeat=False)
#plt.show()
print('SAVING ANIMATION')
writervideo = animation.FFMpegWriter(fps=3)
ani.save('runs71_73_66_LG.mp4', writer=writervideo)
print('FINISHED')
plt.close()
