# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys

from matplotlib import rcParams
rcParams.update({'font.size': 18,'font.weight':'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')


N = 4


dctcp=[0.6,1.3,2.8,4.3]
updctcp=[0.1,0.23,0.34,0.45]
downdctcp=[0.3,0.24,0.22,0.15]


d2tcp=[0.56,1.2,2.72,3.9]
upd2tcp=[0.2,0.13,0.34,0.15]
downd2tcp=[0.3,0.24,0.22,0.15]


lpd=[0.52,1.0,2.47,3.6]
uplpd=[0.2,0.13,0.24,0.15]
downlpd=[0.2,0.13,0.14,0.1]






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
ax.legend((rects1[0], rects2[0],rects3[0]), ('DCTCP', 'L2DCT','LPD'),loc=2)
ax.set_ylabel('AFCT(ms)')
ax.set_ylim([0,8])


fig.savefig("fct_1.eps",dpi=1000)



plt.figure(2)


dctcp=[1.6,2.3,3.8,5.3]
updctcp=[0.1,0.23,0.34,0.45]
downdctcp=[0.3,0.24,0.22,0.15]


d2tcp=[1.26,2.2,3.72,4.9]
upd2tcp=[0.2,0.13,0.34,0.15]
downd2tcp=[0.3,0.24,0.22,0.15]


lpd=[1.02,2.0,2.47,3.6]
uplpd=[0.2,0.13,0.24,0.15]
downlpd=[0.2,0.13,0.14,0.1]




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
ax.legend((rects1[0], rects2[0],rects3[0]), ('DCTCP', 'L2DCT','LPD'),loc=2)
ax.set_ylabel('AFCT(ms)')
ax.set_ylim([0,8])


fig.savefig("fct_2.eps",dpi=1000)


#plt.show()