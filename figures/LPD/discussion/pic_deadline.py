# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys

from matplotlib import rcParams
rcParams.update({'font.size': 18,'font.weight':'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')


N = 4


dctcp=[1.2,2.5,3.5,4.3]
updctcp=[0.1,0.1,0.5,1.0]
downdctcp=[0.1,0.5,0.5,1.0]


d2tcp=[0.25,0.5,1.4,2.5]
upd2tcp=[0.1,0.1,0.5,1.0]
downd2tcp=[0.1,0.5,0.5,1.0]


lpd=[0,0.4,1.0,1.5]
uplpd=[0.1,0.1,0.5,1.0]
downlpd=[0.1,0.5,0.5,1.0]








plt.figure(1)


ind = np.arange(N)  # the x locations for the groups
width = 0.2    # the width of the bars

fig, ax = plt.subplots(dpi=1000)
rects1 = ax.bar(ind, dctcp, width, hatch='/',color='#ADFF2F',yerr=[updctcp,downdctcp],ecolor='k')

rects2 = ax.bar(ind+width, d2tcp, width, hatch="//",color='r',yerr=[upd2tcp,downd2tcp],ecolor='k')


rects3 = ax.bar(ind+2*width, lpd, width, hatch='-',color='k',yerr=[uplpd,downlpd],ecolor='k')




# add some text for labels, title and axes ticks
ax.set_xlabel('flow size(KB)')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('50', '100', '150', '200') )
ax.legend((rects1[0], rects2[0],rects3[0]), ('DCTCP', 'D2TCP','LPD'),loc=2)
ax.set_ylabel('missing deadline(%)')
ax.set_ylim([0,8])


fig.savefig("miss_deadline_1.eps",dpi=1000)
#plt.show()

plt.figure(2)

dctcp=[2.2,4.5,5.5,6.3]
updctcp=[0.1,0.1,0.5,1.0]
downdctcp=[0.1,0.5,0.5,1.0]


d2tcp=[1.25,2.5,3.4,4.5]
upd2tcp=[0.1,0.1,0.5,1.0]
downd2tcp=[0.1,0.5,0.5,1.0]


lpd=[0,1.4,3.0,2.5]
uplpd=[0.1,0.1,0.5,1.0]
downlpd=[0.1,0.5,0.5,1.0]





ind = np.arange(N)  # the x locations for the groups
width = 0.2    # the width of the bars

fig, ax = plt.subplots(dpi=1000)
rects1 = ax.bar(ind, dctcp, width, hatch='/',color='#ADFF2F',yerr=[updctcp,downdctcp],ecolor='k')

rects2 = ax.bar(ind+width, d2tcp, width, hatch="//",color='r',yerr=[upd2tcp,downd2tcp],ecolor='k')


rects3 = ax.bar(ind+2*width, lpd, width, hatch='-',color='k',yerr=[uplpd,downlpd],ecolor='k')




# add some text for labels, title and axes ticks
ax.set_xlabel('flow size(KB)')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('50', '100', '150', '200') )
ax.legend((rects1[0], rects2[0],rects3[0]), ('DCTCP', 'D2TCP','LPD'),loc=2)
ax.set_ylabel('missing deadline(%)')
ax.set_ylim([0,8])


fig.savefig("miss_deadline_2.eps",dpi=1000)

