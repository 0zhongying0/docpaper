# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from pylab import * 

from matplotlib import rcParams
rcParams.update({'font.size': 18,'weight'  : 'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')
N=9

threshold_lax=0.6
threshold_tight=0.3
DMIN=0.05
DMAX=0.1
f1=0.0
f2=0.5
t=np.linspace(0,2,10000);


def penalty(now):
    if(now > threshold_lax):
        return DMAX;
    elif(now < threshold_tight):
        return DMIN;
    else:
        return DMIN+(now-threshold_tight)*(DMAX-DMIN)/(threshold_lax-threshold_tight)


ratio=[];

for i in range(10000):
    dur1=t[i]-f1
    dur2=t[i]-f2
    p1=penalty(dur1)
    p2=penalty(dur2)
    if(dur2<0):
        ratio.append(0)
    else:
        print p2,p1
        ratio.append(float(p1)/float(p2))



filename="2"
time=[]
r1=[]
r2=[]
r3=[]
##now begin to read DCTCP
fp=open(filename,"r")
totaline = fp.readlines()
for line in totaline:
        array = line.split()
        time.append(float(array[0]))
        r1.append(float(array[1]))
        r2.append(float(array[2]))
        r3.append(float(array[2])/float(array[1]))



plt.figure(1)
plot(time,r1,linewidth=1, label="flow1",color='green')
plot(time,r2,linewidth=1, label="flow2",color='blue')

xlim(0.6,1.3)
ylim(0,11000)
ylabel('rate(Mbps)')
xlabel('time(s)')

legend(loc=1)

savefig("rate.eps",dpi=1000)

plt.figure(2)
plot(time,r3,linewidth=1, label="ratio",color='green')
plot(t,ratio,linewidth=1, label="d2/d1",color='b')
ylabel('ratio')
xlabel('time(s)')
xlim(0.6,1.3)
ylim(0,4)


legend(loc=1)

savefig("ratio.eps",dpi=1000)

