# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from pylab import * 

from matplotlib import rcParams
rcParams.update({'font.size': 18,'weight'  : 'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')


x=[]
fluidw1=[]
fluidw2=[]
nsw1=[]
nsw2=[]

##now begin to read DCTCP
fp=open("average2.txt","r")
totaline = fp.readlines()
for line in totaline:
        array = line.split()
        dctcp.append(float(array[0]))
        fluidw1.append(float(array[1]))
        fluidw2.append(float(array[2]))
        nsw1.append(float(array[3]))
        nsw2.append(float(array[4]))

plt.figure(1)

#plot(x,downdctcp,linestyle='dashed', marker='o',linewidth=3,markerfacecolor='blue', markersize=12,label="DCTCP");
plot(x,downl2dct,linestyle='dashed', marker='<',linewidth=3,markerfacecolor='green', markersize=12,label="fluid model",color='green')
plot(x,downpfabric,linestyle='dashed', marker='>',linewidth=3,markerfacecolor='black', markersize=12,label="ns-2",color='black')

xlim(0,200)
ylim(0,10)

xlabel('Dmax')
ylabel('w1/w2')

savefig("ratio.eps",dpi=1200)