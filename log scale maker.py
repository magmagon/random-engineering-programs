import numpy as np
import csv

time1 = -10000
time2 = 100000
#number of data points
pts = int(20)

list_num = []

interval = (np.log10(time2) - np.log10(np.abs(time1))) / (pts - 1)

for i in range(pts):
    x = np.power(
        10, (np.log10(time1) + (i*interval))
    )
    list_num.append(x)

print(list_num)

with open("C:\\Users\\seagu\\OneDrive\\Documents\\random python programs\\log_scale.csv", "w", newline="") as log_scale:
    writer = csv.writer(log_scale, delimiter = " ")
    for item in list_num:
        print(item)
        writer.writerow([item])