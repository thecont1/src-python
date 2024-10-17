import numpy as np

with open("/Users/home/DEV/scaler/python/src/nps.txt", 'r') as f:
    nps_data = np.array(f.readlines(), dtype=int)

detractors_perc = 100 * nps_data[nps_data <= 6].size / nps_data.size
promoters_perc = 100 * nps_data[nps_data >= 9].size / nps_data.size

nps = round(promoters_perc - detractors_perc, 2)

print(f"Net Promoter Score = {nps}%")