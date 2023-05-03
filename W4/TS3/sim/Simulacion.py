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
ep = (10**0.1 -1)**(1/2)

my_tf = TransferFunction( [ep**(-2/3)], [1, 2*ep**(-1/3), 2*ep**(-2/3), ep**-1] )


plt.close('all')

bodePlot(my_tf, fig_id=1)

pzmap(my_tf, fig_id=2) #S plane pole/zero plot

GroupDelay(my_tf, fig_id=3)