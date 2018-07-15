# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 13:52:35 2018

@author: yasushi
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-np.pi, np.pi, 1000)
x1 = np.sin(2*t)
x2 = np.cos(2*t)

#fig, (axL, axR) = plt.subplots(ncols=2, figsize=(10,4))
fig, (axL, axR) = plt.subplots(nrows=2, figsize=(5,10))

axL.plot(t, x1, linewidth=2)
axL.set_title('sin')
axL.set_xlabel('t')
axL.set_ylabel('x')
axL.set_xlim(-np.pi, np.pi)
axL.grid(True)

axR.plot(t, x2, linewidth=2)
axR.set_title('cos')
axR.set_xlabel('t')
axR.set_ylabel('x')
axR.set_xlim(-np.pi, np.pi)
axR.grid(True)

fig.show()