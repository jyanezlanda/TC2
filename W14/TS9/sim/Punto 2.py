#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:39:40 2023

@author: joaquin
"""

from pytc2.sintesis_dipolo import cauer_LC, foster, remover_polo_dc
from pytc2.dibujar import dibujar_cauer_LC, dibujar_foster_serie, dibujar_foster_derivacion
import sympy as sp

s = sp.symbols('s', complex=True)

FF = (3*s*(s**2 + 7/3))/((s**2 + 2)*(s**2 + 5))

k0, ZZ = remover_polo_dc(1/ FF, omega_zero= 1)




FF = 1/(1/FF - ZZ)
#FF = (3*s*(s**2 + 7/3))/((s**2 + 1)*(s**2 + 3))

# Implementaremos F mediante Cauer 2 o remociones continuas en cero
# Implementaremos F mediante Cauer 2 o remociones continuas en cero


k0, koo, ki_wi, _, FF_foster = foster(FF)
dibujar_foster_derivacion(k0, koo, ki_wi, y_exc = FF)
