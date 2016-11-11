import sys
sys.path.insert(0, '/Users/erezcohen/larlite/UserDev/mySoftware/MySoftwarePackage/mac')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("csv_data/best_measurements.csv")
H_5_100 , H_5_160 , H_8_100 , H_8_160 = np.zeros((4,6)) , np.zeros((4,6)) , np.zeros((4,6)) , np.zeros((4,6))

print data

efficiency = data['efficiency [%]']
timing_res = data['time-res([L+R]/2) [ps]']
sci = data['scintillator']
width = data['width[mm]']
SiPM = data['SiPMs']
threshold = data['cfd-threshold [mV]']


for i in range(len(data)):

    t = timing_res[i]
    
    
    if sci[i]=='EJ204':
        scintillator_type = 0
    elif sci[i]=='EJ204 coated':
        scintillator_type = 1
    elif sci[i]=='BC420':
        scintillator_type = 2
    elif sci[i]=='BC422':
        scintillator_type = 3
    elif sci[i]=='BC422 12um AirGap':
        scintillator_type = 4
    elif sci[i]=='BC422 6um Air,6um Al-Milar':
        scintillator_type = 5
    if sci[i]=='B404':
        scintillator_type = 0
    elif sci[i]=='BC418':
        scintillator_type = 1



    if SiPM[i]=='S13360-3050PE':
        SiPM_type = 0
    elif SiPM[i]=='S13360-3025PE':
        SiPM_type = 1
    elif SiPM[i]=='S12572-025P':
        SiPM_type = 2
    elif SiPM[i]=='AdvanSiD':
        SiPM_type = 3

    print scintillator_type , SiPM_type , t , " ps"

    if width[i]==5:
        H_5 [ SiPM_type , scintillator_type ] = t
    if width[i]==8:
        H_8 [SiPM_type , scintillator_type  ] = t

H_5 [ H_5[:,:] == 0 ] = 'NAN'
H_8 [ H_8[:,:] == 0 ] = 'NAN'

sns.set(font_scale=1.5)
sns.set_style({"font.family":[u"serif"]})

fig = plt.figure()
plt.subplot(1,2,1)
fig.subplots_adjust(left=0.08)
fig.subplots_adjust(bottom=0.11)
fig.subplots_adjust(top=0.94)
fig.subplots_adjust(right=0.99 , wspace=0.05)


#ax = plt.axes()
heatmap_5 = sns.heatmap(H_5,annot=True,fmt=".0f"
            ,xticklabels=['EJ204','EJ204 coated','BC420','BC422','BC422 \n 12'+r'$\mu$'+'m Air','BC422 \n6'+r'$\mu$'+'m Air\n6'+r'$\mu$'+'m AlBoPET']
            ,yticklabels=['S13360-\n3050PE','S13360-\n3025PE','S12572-\n025P','AdvanSiD']
            ,linewidths=1.,cbar=False)
heatmap_5.set_title('5 mm wide')

plt.yticks(rotation=0)
plt.subplot(1,2,2)
fig.subplots_adjust(left=0.08)
fig.subplots_adjust(bottom=0.11)
fig.subplots_adjust(top=0.94)
fig.subplots_adjust(right=0.99 , wspace=0.05)


heatmap_8 = sns.heatmap(H_8,annot=True,fmt=".0f"
            ,xticklabels=['','','','BC422']
            ,yticklabels=['','','','','','']
            ,linewidths=1.,cbar=False)
plt.yticks(rotation=0)
heatmap_8.set_title('8 mm wide')

plt.show()

file_name = "timing_resolution_heatmap"
save_path = "/Users/erezcohen/Desktop/"

plt.savefig(save_path + file_name + ".pdf")









