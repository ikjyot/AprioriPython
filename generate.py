from random import *
import numpy as np
import csv
import os

ip_files = []
for file in os.listdir('./'):
    if file.startswith("db"):
        ip_files.append(file)

for ip in ip_files:
    data = []
    f_ob = open(ip, 'r', encoding='ascii')
    read_lines = csv.reader(f_ob)
    for row in read_lines:
        data.append(row[0])

    data_cp = data[0:10]
    transactions = []
    for i in range(1, 21):
        temp_list = []
        np.random.shuffle(data_cp)
        transactions.append(data_cp[:randint(2, 6)])

    op = 'tr_' + ip

    with open(op, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(transactions)

