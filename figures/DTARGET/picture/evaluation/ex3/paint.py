# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats

from matplotlib import rcParams
rcParams.update({'font.size': 18,'font.weight':'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')


if __name__=='__main__':


    bar1=[2.4,2.2,2.3,2.5,2.6]
    bar2=[2.2,2,2.1,1.9,2.1]

    up=[0.3,0.2,0.1,0.11,0.12]

    down=[0.3,0.2,0.1,0.11,0.12]



    N=5
    ind = np.arange(N)  # the x locations for the groups
    width = 0.2       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, bar1, width,hatch="//",color='k',ecolor='k')
    rects2 = ax.bar(ind+width, bar2, width,  yerr=[down,up],hatch='-',color='blue',ecolor='k')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(('Total','[2,6)','[6,10)','[10,14)','[14,20)'))
    ax.legend((rects1[0],rects2[0]), ('2-approximate','online'),loc=2)
    ax.set_ylabel('Improvement over TCP',fontsize=18,fontweight='bold')
    ax.set_xlabel('Trunk number',fontsize=18,fontweight='bold')
    ax.set_ylim([0,4])
    fig.savefig("on_off_2.eps")




    bar1=[2.0,1.8,1.9,2.2,2.4]
    bar2=[1.8,1.7,1.75,1.9,2.1]

    up=[0.3,0.2,0.1,0.11,0.12]

    down=[0.3,0.2,0.1,0.11,0.12]



    N=5
    ind = np.arange(N)  # the x locations for the groups
    width = 0.2       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, bar1, width,  yerr=[down,up],hatch="//",color='k',ecolor='k')
    rects2 = ax.bar(ind+width, bar2, width,  yerr=[down,up],hatch='-',color='blue',ecolor='k')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(('Total','[2,6)','[6,10)','[10,14)','[14,20)'))
    ax.legend((rects1[0],rects2[0]), ('2-approximate','online'),loc=2)
    ax.set_ylabel('Improvement over TCP',fontsize=18,fontweight='bold')
    ax.set_xlabel('Trunk number',fontsize=18,fontweight='bold')
    ax.set_ylim([0,4])
    fig.savefig("on_off_3.eps")





