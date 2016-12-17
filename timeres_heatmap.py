import sys
sys.path.insert(0, '/Users/erezcohen/larlite/UserDev/mySoftware/MySoftwarePackage/mac')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("csv_data/best_measurements.csv")
H_5_100 , H_5_161 , H_8_100 , H_8_161 , H_4_100 , H_4_161   = np.zeros((4,6)) , np.zeros((4,6)) , np.zeros((4,6)) , np.zeros((4,6)) , np.zeros((4,6)) , np.zeros((4,6))
#H_4_100 , H_4_161 , H_5_100 , H_5_161 , H_8_100 , H_8_161  = np.zeros((4,2)) , np.zeros((4,6)) , np.zeros((4,6)) , np.zeros((4,4)) , np.zeros((4,4))

#print data

efficiency  = data['efficiency [%]']
timing_res  = data['time-res([L+R]/2) [ps]']
sci         = data['scintillator']
width       = data['width[mm]']
length      = data['length[mm]']
SiPM        = data['SiPMs']
threshold   = data['cfd-threshold [mV]']

def plot_heatmap( i , H , xticklabels , yticklabels , title ):
    plt.subplot(2,3,i)
#    fig.subplots_adjust(subplots_adjust_pars)

    heatmap = sns.heatmap(H,annot=True,fmt=".0f" ,xticklabels=xticklabels ,yticklabels=yticklabels ,linewidths=1.,cbar=False)
    heatmap.set_title(title)


for i in range(len(data)):

    t = timing_res[i]
    
    
    if sci[i]=='EJ204':
        scintillator_type = 0
    elif sci[i]=='EJ204 coated':
        scintillator_type = 3
    elif sci[i]=='BC420':
        scintillator_type = 2
    elif sci[i]=='BC422':
        scintillator_type = 1
    elif sci[i]=='BC422 12um AirGap':
        scintillator_type = 4
    elif sci[i]=='BC422 6um Air,6um Al-Milar':
        scintillator_type = 5
    elif sci[i]=='BC404':
        scintillator_type = 0
    elif sci[i]=='BC418':
        scintillator_type = 3



    if SiPM[i]=='S13360-3050PE':
        SiPM_type = 0
    elif SiPM[i]=='S13360-3025PE':
        SiPM_type = 1
    elif SiPM[i]=='S12572-025P':
        SiPM_type = 2
    elif SiPM[i]=='AdvanSiD':
        SiPM_type = 3
    elif SiPM[i]=='S13360-3075PE':
        SiPM_type = 1

#    print scintillator_type , SiPM_type , t , " ps"

    if width[i]==5 and length[i]==100:
        H_5_100 [ SiPM_type , scintillator_type ] = t
    if width[i]==5 and length[i]==161.5:
        H_5_161 [ SiPM_type , scintillator_type ] = t
    if width[i]==8 and length[i]==100:
        H_8_100 [SiPM_type , scintillator_type  ] = t
    if width[i]==8 and length[i]==161.5:
        H_8_161 [ SiPM_type , scintillator_type ] = t
    if width[i]==4 and length[i]==100:
        H_4_100 [ SiPM_type , scintillator_type ] = t
    if width[i]==4 and length[i]==161.5:
        H_4_161 [ SiPM_type , scintillator_type ] = t



H_5_100 [ H_5_100[:,:] == 0 ] = 'NAN'
H_5_161 [ H_5_161[:,:] == 0 ] = 'NAN'
H_8_100 [ H_8_100[:,:] == 0 ] = 'NAN'
H_8_161 [ H_8_161[:,:] == 0 ] = 'NAN'
H_4_100 [ H_4_100[:,:] == 0 ] = 'NAN'
H_4_161 [ H_4_161[:,:] == 0 ] = 'NAN'

sns.set(font_scale=1.0) #1.5
sns.set_style({"font.family":[u"serif"]})

fig = plt.figure(figsize=(15,10))

plot_heatmap( 1 ,
             H_4_100,
             xticklabels=['BC404','BC422',],
             yticklabels=['S13360-\n3050PE','S13360-\n3075PE','','AdvanSiD'],
             title = '4 mm wide, 100 mm long')

plot_heatmap( 2 ,
             H_5_100,
             xticklabels=['EJ204','EJ204 coated','BC420','BC422','BC422 \n 12'+r'$\mu$'+'m Air','BC422 \n6'+r'$\mu$'+'m Air\n6'+r'$\mu$'+'m AlBoPET'],
             yticklabels=['S13360-\n3050PE','S13360-\n3025PE','S12572-\n025P','AdvanSiD'],
             title = '5 mm wide, 100 mm long')

plot_heatmap( 3 ,
             H_8_100,
             xticklabels=['','','','BC422','',''],
             yticklabels=['S13360-\n3050PE','S13360-\n3025PE','S12572-\n025P','AdvanSiD'],
             title = '8 mm wide, 100 mm long')
fig.subplots_adjust(left=0.08 ,bottom=0.11 , top=0.94 , right=0.99 , wspace=0.05)

plot_heatmap( 4 ,
             H_4_161,
             xticklabels=['BC404','BC422',],
             yticklabels=['S13360-\n3050PE','S13360-\n3075PE','','AdvanSiD'],
             title = '4 mm wide, 161.5 mm long')
fig.subplots_adjust(left=0.08 ,bottom=0.11 , top=0.94 , right=0.99 , wspace=0.05)

plot_heatmap( 5 ,
             H_5_161,
             xticklabels=['BC404','BC418','BC420','BC422'],
             yticklabels=['S13360-\n3050PE','S13360-\n3025PE','S12572-\n025P','AdvanSiD'],
             title = '5 mm wide, 161.5 mm long')
fig.subplots_adjust(left=0.08 ,bottom=0.11 , top=0.94 , right=0.99 , wspace=0.05)

plot_heatmap( 6 ,
             H_8_161,
             xticklabels=['BC404','BC418','BC420','BC422'],
             yticklabels=['S13360-\n3050PE','S13360-\n3025PE','S12572-\n025P','AdvanSiD'],
             title = '8 mm wide, 161.5 mm long')
fig.subplots_adjust(left=0.08 ,bottom=0.11 , top=0.94 , right=0.99 , wspace=0.05)


plt.show()

#fig.savefig("/Users/erezcohen/Desktop/timing_resolution_heatmap.pdf")









