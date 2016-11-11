# create a visual plot from all Tiko' measurements during May-Aug 2016

import ROOT , os, sys , math , os.path
from ROOT import TPlots , TAnalysis
from rootpy.interactive import wait
import pandas as pd
sys.path.insert(0, '/Users/erezcohen/larlite/UserDev/mySoftware/MySoftwarePackage/mac')
ROOT.gStyle.SetOptStat(0000)
import numpy as np
import input_flags
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import from_levels_and_colors


flags = input_flags.get_args()


data = pd.read_csv("csv_data/best_measurements.csv")


if flags.verbose>1:
    print data
efficiency = data['efficiency [%]']
t_axis_5 = []
t_axis_8 = []
timing_res = data['time-res([L+R]/2) [ps]']
x_axis_5 = []
x_axis_8 = []
scint = []
sci = data['scintillator']
width = data['width[mm]']
z_axis_5 = []
z_axis_8 = []
SiPM = data['SiPMs']
threshold = data['cfd-threshold [mV]']
c = []
m = []

if flags.verbose>1:
    print efficiency
    print timing_res

fig = plt.figure()


for i in range(len(data)):
    if sci[i]=='EJ204':
        scintillator_type = 0
    elif sci[i]=='EJ204 coated':
        scintillator_type = 1
    if sci[i]=='BC420':
        scintillator_type = 2
    if sci[i]=='BC422':
        scintillator_type = 3 
    scintillator_type = scintillator_type +0.1


    if SiPM[i]=='S13360-3050PE':
        SiPM_type = 0
    elif SiPM[i]=='S12572-3025PE':
        SiPM_type = 1
    elif SiPM[i]=='S13360-3025PE':
        SiPM_type = 2
    elif SiPM[i]=='S12572-025P':
        SiPM_type = 3
    elif SiPM[i]=='AvanSiD':
        SiPM_type = 4
   
   
    if width[i]==5:
        x_axis_5.append( scintillator_type )
        z_axis_5.append( SiPM_type )
        t_axis_5.append( timing_res[i] )
        if flags.verbose>1:
            print "5 mm"
            print sci[len(z_axis_5)-1] , SiPM[len(z_axis_5)-1]
            print x_axis_5[len(z_axis_5)-1] , z_axis_5[len(z_axis_5)-1]

    if width[i]==8:
        x_axis_8.append(scintillator_type )
        z_axis_8.append( SiPM_type )
        t_axis_8.append( timing_res[i] )

        if flags.verbose>1:
            print "8 mm"
            print sci[len(x_axis_8)-1] , SiPM[len(x_axis_8)-1]
            print x_axis_8[len(z_axis_8)-1] , z_axis_8[len(z_axis_8)-1]

#ax.scatter(x_axis[i] , timing_res[i] , z_axis[i])# , color=c[i], marker=m[i])
plt.subplot(1,2,1)
hist= plt.hist2d( x_axis_5 , z_axis_5  , weights = t_axis_5 , cmap=plt.get_cmap('YlOrBr') , range=[(-1,4),(-1,6)] , bins = [50,50]) # ,bins = [10,10]
plt.colorbar()
plt.xticks([0,1,2,3], ['EJ204','EJ204 coated','BC420','BC422'])
plt.yticks([0,1,2,3,4], ['S13360-3050PE','S12572-3025PE','S13360-3025PE','S12572-025P','AvanSiD'])
#plt.xticks(x_axis_5, sci)
plt.yticks(z_axis_5, SiPM)


plt.subplot(1,2,2)
hist= plt.hist2d( x_axis_8 , z_axis_8  , weights = t_axis_8,cmap=plt.get_cmap('YlOrBr'))
plt.colorbar()
#plt.xticks(x_axis_8, sci)
#plt.yticks(z_axis_8, SiPM)

plt.show()
fig.savefig('timingRes_vs_efficiency.pdf')

