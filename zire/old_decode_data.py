import struct
import csv
import matplotlib.pyplot as plt
import os
import pandas as pd
import sys
import numpy as np
import time

#############################################
run = 9         #################### <------- RUN
id_asic = 2     # 0, 1, 2, 3
id_ch = 23      # 0, 1, ..., 31 
bin = 1024      # 1024, ..., 16383
parziale = 100
#############################################
data_path = "./calo_calibration/run_58/data"
#############################################

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
    total_packets = len(data) // packet_size
    packets_opened = 0
    start_time = time.time()
    last_progress_time = start_time

    while offset + packet_size <= len(data):
        # Estrai il pacchetto corrente
        packet_data = data[offset:offset + packet_size]

        # Decodifica i dati del pacchetto
        data_buffer = struct.unpack("Q" * 67, packet_data)

        # Esegui l'analisi del pacchetto
        decode_data_buffer(data_buffer)

        # Aggiorna l'offset per il prossimo pacchetto
        offset += packet_size       
        packets_opened += 1

        # Calcola il progresso
        progress = packets_opened / total_packets * 100

        # Mostra il progresso una volta ogni 10 secondi
        current_time = time.time()
        if current_time - last_progress_time >= 10:
            print(f"Decoding: {progress:.2f}%")
            last_progress_time = current_time

        if progress >= parziale:
            break

def plot_ch(file_path, asic, ch, bin):

    # col 6 is first ch
    id = (asic*32+ch)*2+4
    df_lg = (pd.read_csv(file_path + ".csv", header=None, low_memory=False)[id][1:]).astype(int)
    df_hg = (pd.read_csv(file_path + ".csv", header=None, low_memory=False)[id+1][1:]).astype(int)

    bins = np.arange(0, 16384, int(16384/bin))
    lg = np.digitize(df_lg, bins)
    hg = np.digitize(df_hg, bins)


    # Dimensione
    plt.figure(figsize=(20, 10))
    
    # Effettua il plot del primo DataFrame
    plt.hist(lg, label=f'Asic {asic} CH{ch} LG', bins=np.arange(0, bin, 1))
    plt.hist(hg, label=f'Asic {asic} CH{ch} HG', bins=np.arange(0, bin, 1))

    # Title
    plt.title(f'Asic {asic} CH{ch}')

    # Aggiungi una legenda al plot
    plt.legend()

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
print("CHARGING PLOT...")
#plot_ch (data_path, id_asic, id_ch, bin)

print("END")