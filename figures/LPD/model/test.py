from os import listdir
from os.path import isfile, join
from pylab import * 
from numpy import * 
from matplotlib import rcParams
rcParams.update({'font.size': 14,'font.weight':'bold'})





plt.figure(1) # create fig1 congestion window

plt.ylim([80,101])
window=[4,8,10,12,15,20,22,25,30]
lpd1=[95,96,96.50,97.00,99.00,100,100,100,100]
lpd2=[94.00,95,95,96,98,99,100,100,100]

plt.xlabel('Marking Threshold K (% of BDP))')

plt.ylabel('Throughput(%)')

plot(window,lpd1,color='b',marker='<',markersize=10,linewidth=3,label='LPD (N=2)')
plot(window,lpd2,color='k',marker='>',markersize=10,linewidth=3,label='LPD (N=20)')


plt.legend(loc=4)
plt.savefig('throughput.pdf')



plt.figure(2) # create fig1 congestion window

plt.ylim([-0.6,0])
tmax=[10,15,20,25,30,35,40,45,50,55]
g1=[-0.12,-0.15,-0.17,-0.18,-0.19,-0.22,-0.25,-0.28,-0.32,-0.35]
g2=[-0.14,-0.17,-0.19,-0.20,-0.22,-0.25,-0.28,-0.29,-0.34,-0.38]
g3=[-0.17,-0.19,-0.20,-0.22,-0.25,-0.28,-0.29,-0.33,-0.38,-0.40]

plt.xlabel('tmax')

plt.ylabel('qmin(fraction of CR)')

plot(tmax,g1,color='b',marker='<',markersize=10,linewidth=3,label='g=0.01')
plot(tmax,g2,color='k',marker='>',markersize=10,linewidth=3,label='g=0.05')
plot(tmax,g3,color='r',marker='>',markersize=10,linewidth=3,label='g=0.1')

plt.legend(loc=4)
plt.savefig('qmin.pdf')




	
show()