import struct
import csv
import matplotlib.pyplot as plt
import os
import pandas as pd
import sys
import numpy as np
import time

#############################################
run = 9   #################### <------- RUN
#############################################
data_path = "C:/Users/feliciabarbato/Desktop/Zirettino/RUNS/run_" + str(run) + "/data"
#############################################

pst = [
    ['pst_1_1', 22, 23],
    ['pst_1_2', 13, 22],
    ['pst_1_3', 12, 21],
    ['pst_2_1', 16, 15],
    ['pst_2_2', 17, 16],
    ['pst_2_3', 18, 17],
    ['pst_3_1', 21, 19],
    ['pst_3_2', 14, 18],
    ['pst_3_3', 15, 10],
    ['pst_4_1', 19, 14],
    ['pst_4_2', 0, 20],
    ['pst_4_3', 1, 11],
    ['pst_5_1', 20, 7],
    ['pst_5_2', 3, 8],
    ['pst_5_3', 2, 9],
    ['pst_6_1', 6, 13],
    ['pst_6_2', 5, 5],
    ['pst_6_3', 4, 6],
    ['pst_7_1', 23, 2],
    ['pst_7_2', 11, 3],
    ['pst_7_3', 10, 4],
    ['pst_8_1', 9, 12],
    ['pst_8_2', 8, 0],
    ['pst_8_3', 7, 1]
]

def write_to_csv(file_path, data):
    fieldnames = ['TIMESTAMP', 'TRIGGERID', 'TRIGGER COUNTS', 'VALID', 'FLAG']
    for x in range(4):
        for y in range(32):
            fieldnames.append(f'Asic{x}_CH{y}_HG')
            fieldnames.append(f'Asic{x}_CH{y}_LG')

    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Scrivi l'intestazione nel file
        writer.writeheader()
        
        # Scrivi i dati
        for row in data:
            writer.writerow(row)

def decode_data_buffer(data_buffer):
    timestamp = (((data_buffer[0] & 0xFFFFFFFF) << 32) + (data_buffer[0] >> 32))
    trigger_id = (data_buffer[1] & 0xFFFFFFFF)
    trigger_counts = (data_buffer[1] >> 32)
    valid = (data_buffer[2] & 0xFFFFFFFF)
    flag = (data_buffer[2] >> 32)

    for i in range (3, 67):
        temp_lg.append(data_buffer[i] & 0x3FFF)
        temp_hg.append(data_buffer[i] >> 14 & 0x3FFF)
        temp_lg.append((data_buffer[i] >> 32) & 0x3FFF)
        temp_hg.append((data_buffer[i] >> 32) >> 14 & 0x3FFF)


    new_data = {'TIMESTAMP':timestamp, 'TRIGGERID': trigger_id, 'TRIGGER COUNTS': trigger_counts, 'VALID': valid, 'FLAG': flag}

    for x in range(4):
        for y in range(32):
            asic_ch_hg = f'Asic{x}_CH{y}_HG'
            asic_ch_lg = f'Asic{x}_CH{y}_LG'
            new_data[asic_ch_hg] = temp_hg[(x*32)+(y)]
            new_data[asic_ch_lg] = temp_lg [(x*32)+(y)]   
    data_ts.append(new_data)
    temp_hg.clear()
    temp_lg.clear()

def open_data(file_path):
    with open(file_path + ".bin", "rb") as file:
        data = file.read()

    # Ottieni la dimensione del pacchetto
    packet_size = struct.calcsize("Q" * 67)

    # Decodifica e analizza tutti i pacchetti nel file
    offset = 0

    while offset + packet_size <= len(data):
        # Estrai il pacchetto corrente
        packet_data = data[offset:offset + packet_size]

        # Decodifica i dati del pacchetto
        data_buffer = struct.unpack("Q" * 67, packet_data)

        # Esegui l'analisi del pacchetto
        decode_data_buffer(data_buffer)

        # Aggiorna l'offset per il prossimo pacchetto
        offset += packet_size       


def plot_ch(file_path, bin):

    ch_all=0
    fig, axs = plt.subplots(4, 6, figsize=(16, 8))
    A=[]
    B=[]

    for i in range(32):
        id = (0*32+ch_all)*2+5
        df_A = (pd.read_csv(file_path + ".csv", header=None, low_memory=False)[id][1:]).astype(int)
        id = (1*32+ch_all)*2+5
        df_B = (pd.read_csv(file_path + ".csv", header=None, low_memory=False)[id][1:]).astype(int)

        bins = np.arange(0, 16384, int(16384/bin))
        A.append(np.digitize(df_A, bins))
        B.append(np.digitize(df_B, bins))

        ch_all += 1

    # Assegnazione dei valori agli array A e B
    A_pst=[]
    B_pst=[]
    labels=[]
    for entry in pst:
        label, index_A, index_B = entry
        A_pst.append(A[index_A])
        B_pst.append(A[index_B])
        labels.append(label)

    print("CHARGING PLOT...")
    for i in range (24):
        row = i // 6
        col = i % 6
        ax = axs[row, col]

        ax.hist(A_pst[i], bins=np.arange(0, bin, 1), label="3x3")
        ax.hist(B_pst[i], bins=np.arange(0, bin, 1), label="1x1")


        # Posiziona il testo
        text_x = 0.95
        text_y = 0.85

        # Posiziona la legenda
        legend_x = 0.95
        legend_y = 0.7

        ax.text(text_x, text_y, f'{labels[i]}', transform=ax.transAxes, ha='right', va='top',
                bbox=dict(facecolor='white', edgecolor='black'))

        ax.legend(loc='upper left', bbox_to_anchor=(legend_x, legend_y))

    # Aumenta lo spazio tra i subplots per evitare sovrapposizioni
    plt.tight_layout()

    # Mostra il plot
    plt.show()

# Carica i dati dal file binario
print("START")
data_ts = []
temp_hg = []
temp_lg = []

if not os.path.exists(data_path + ".bin"):
    print("data file not found!")
    sys.exit()

if not os.path.exists(data_path + ".csv"):
    # Apre il file e decodifica i dati
    open_data(data_path)
    print("DATA DECODED")
    # Scrivi i dati nel file CSV
    write_to_csv(data_path + '.csv', data_ts)
    print("DATA WRITTEN ON CSV")

# Plot one channel HG and LG
print("CHARGING DATA...")
plot_ch (data_path, 4096)

print("END")