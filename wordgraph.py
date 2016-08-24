#!/usr/bin/python

import sys
import string
import matplotlib.pyplot as plt
fp = open(sys.argv[1], 'r')
para = fp.read()
xaxis = range(1, 27)
yaxis = []
for i in string.lowercase[:]:
    yaxis.append(para.count(i))
plt.plot(xaxis, yaxis)
plt.show()
print ans
fp.close()
