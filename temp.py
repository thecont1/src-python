import numpy as np

labels = ['Date', 'Step Count', 'Mood', 'Calories Burnt', 'Hours of Sleep', 'Activity Status']
data = np.loadtxt("/Users/home/Downloads/fit.txt", dtype='str')

print(data)

