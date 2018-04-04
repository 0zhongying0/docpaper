# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys

from matplotlib import rcParams
rcParams.update({'font.size': 18,'font.weight':'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')


N = 4




d2tcp=[4.7,4.9,5.7,7.8]
upd2tcp=[2,1.3,1.4,1.2]
downd2tcp=[2,1.4,1.4,1.5]


lpd=[9,12,15,22]
uplpd=[2,1.3,1.4,1.2]
downlpd=[2,1.4,1.4,1.5]






plt.figure(1)



ind = np.arange(N)  # the x locations for the groups
width = 0.2    # the width of the bars

fig, ax = plt.subplots(dpi=1000)
rects1 = ax.bar(ind, d2tcp, width, hatch='/',color='#ADFF2F',yerr=[upd2tcp,downd2tcp],ecolor='k')

rects2 = ax.bar(ind+width, lpd, width, hatch="//",color='r',yerr=[uplpd,downlpd],ecolor='k')




# add some text for labels, title and axes ticks
ax.set_xlabel('fan-in-degree')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('10','20','30','40') )
ax.legend((rects1[0], rects2[0]), ('LPD-e', 'TCP'),loc=2)
ax.set_ylabel('missing deadline(%)')
ax.set_ylim([0,25])


fig.savefig("20ms.eps",dpi=1000)






d2tcp=[1,2,3,4]
upd2tcp=[0.5,0.6,0.4,0.6]
downd2tcp=[0.5,0.6,0.4,0.6]


lpd=[5,8,14,19]
uplpd=[0.5,0.6,0.4,0.6]
downlpd=[0.5,0.6,0.4,0.6]






plt.figure(1)



ind = np.arange(N)  # the x locations for the groups
width = 0.2    # the width of the bars

fig, ax = plt.subplots(dpi=1000)
rects1 = ax.bar(ind, d2tcp, width, hatch='/',color='#ADFF2F',yerr=[upd2tcp,downd2tcp],ecolor='k')

rects2 = ax.bar(ind+width, lpd, width, hatch="//",color='r',yerr=[uplpd,downlpd],ecolor='k')




# add some text for labels, title and axes ticks
ax.set_xlabel('fan-in-degree')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('10','20','30','40') )
ax.legend((rects1[0], rects2[0]), ('LPD-e', 'TCP'),loc=2)
ax.set_ylabel('missing deadline(%)')
ax.set_ylim([0,25])


fig.savefig("30ms.eps",dpi=1000)









d2tcp=[0.5,0.6,1,2]
upd2tcp=[0.2,0.2,0.3,0.2]
downd2tcp=[0.2,0.2,0.3,0.2]


lpd=[4,8,10,14]
uplpd=[0.2,0.2,0.3,0.2]
downlpd=[0.2,0.2,0.3,0.2]





plt.figure(1)



ind = np.arange(N)  # the x locations for the groups
width = 0.2    # the width of the bars

fig, ax = plt.subplots(dpi=1000)
rects1 = ax.bar(ind, d2tcp, width, hatch='/',color='#ADFF2F',yerr=[upd2tcp,downd2tcp],ecolor='k')

rects2 = ax.bar(ind+width, lpd, width, hatch="//",color='r',yerr=[uplpd,downlpd],ecolor='k')




# add some text for labels, title and axes ticks
ax.set_xlabel('fan-in-degree')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('10','20','30','40') )
ax.legend((rects1[0], rects2[0]), ('LPD-e', 'TCP'),loc=2)
ax.set_ylabel('missing deadline(%)')
ax.set_ylim([0,25])


fig.savefig("40ms.eps",dpi=1000)

