import numpy as np

labels = ['Date', 'Step Count', 'Mood', 'Calories Burnt', 'Hours of Sleep', 'Activity Status']
data = np.loadtxt("fit.txt", dtype='str')

# Total number of records = 96
len(data)

# No. of 'Sad' and 'Inactive' members = 25
len(data[(data[:,2]=='Sad') & (data[:,5]=='Inactive')])
# No. of 'Happy' and 'Inactive' members = 16
len(data[(data[:,2]=='Happy') & (data[:,5]=='Inactive')])

# No. of 'Sad' and 'Active' members = 4
len(data[(data[:,2]=='Sad') & (data[:,5]=='Active')])
# No. of 'Happy' and 'Active' members = 24
len(data[(data[:,2]=='Happy') & (data[:,5]=='Active')])

# No. of 'Neutral' = 14 'Active' and 13 'Inactive'
len(data[(data[:,2]=='Neutral') & (data[:,5]=='Active')])
len(data[(data[:,2]=='Neutral') & (data[:,5]=='Inactive')])


# Average Step Count of 'Inactive' members = 2710
np.average(data[(data[:,5]=='Inactive')][:,1].astype('int'))
# Average Step Count of 'Active' members = 3227
np.average(data[(data[:,5]=='Active')][:,1].astype('int'))


# Average Step Count of 'Sad' members = 2103
np.average(data[(data[:,2]=='Sad')][:,1].astype('int'),0)
# Average Step Count of 'Neutral' members = 3154
np.average(data[(data[:,2]=='Neutral')][:,1].astype('int'),0)
# Average Step Count of 'Happy' members = 3393
np.average(data[(data[:,2]=='Happy')][:,1].astype('int'),0)



