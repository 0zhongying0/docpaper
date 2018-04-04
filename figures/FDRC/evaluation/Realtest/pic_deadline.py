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


atc=[0.21,0.6,1.1,1.8]
upatc=[0.1,0.1,0.5,1.0]
downatc=[0.1,0.1,0.5,1.0]







ind = np.arange(N)  # the x locations for the groups
width = 0.2    # the width of the bars

fig, ax = plt.subplots(dpi=1000)
rects1 = ax.bar(ind, dctcp, width, hatch='/',color='#ADFF2F',yerr=[updctcp,downdctcp],ecolor='k')

rects2 = ax.bar(ind+width, d2tcp, width, hatch="//",color='r',yerr=[upd2tcp,downd2tcp],ecolor='k')


rects3 = ax.bar(ind+2*width, lpd, width, hatch='-',color='w',yerr=[uplpd,downlpd],ecolor='k')


rects4 = ax.bar(ind+3*width, atc, width,hatch='o', color='k',yerr=[upatc,downatc],ecolor='k')


# add some text for labels, title and axes ticks
ax.set_xlabel('flow size(KB)')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('50', '100', '150', '200') )
ax.legend((rects1[0], rects2[0],rects3[0],rects4[0]), ('dctcp', 'd2tcp','LPD','ATC'),loc=2)
ax.set_ylabel('missing deadline(%)')
ax.set_ylim([0,8])


fig.savefig("miss_deadline_.eps",dpi=1000)
#plt.show()