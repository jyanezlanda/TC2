# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:03:10 2023

@author: Joaquin
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

R1 = 10000
R2 = R1
R3 = 1000
C1 = 1*10**-6

my_tf = TransferFunction( [1,-R2/(R1*C1*R3)], [1, 1/(C1*R3)] )


plt.close('all')

bodePlot(my_tf, fig_id=1)

pzmap(my_tf, fig_id=2) #S plane pole/zero plot

GroupDelay(my_tf, fig_id=3)