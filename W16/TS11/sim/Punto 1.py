#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:08:09 2023

@author: joaquin
"""

from pytc2.sintesis_dipolo import cauer_LC, foster
from pytc2.dibujar import dibujar_cauer_LC, dibujar_foster_serie, dibujar_foster_derivacion
import sympy as sp

s = sp.symbols('s', complex=True)

FF = ((s**2 + 3)*(s**2 + 1))/(s*(s**2 + 2))

k0, koo, ki_wi, _, FF_foster = foster(FF)

dibujar_foster_serie(k0, koo, ki_wi, z_exc = FF )

k0, koo, ki_wi, _, FF_foster = foster(1/FF)
dibujar_foster_derivacion(k0, koo, ki_wi, y_exc = 1/FF)


# Implementaremos F mediante Cauer 2 o remociones continuas en cero
k0, F_cauer_0, rem = cauer_LC(FF, remover_en_inf=False)



#print_latex(a_equal_b_latex_s(a_equal_b_latex_s('F(s)', FF)[1:-1], F_cauer_0 ))


# Tratamos a nuestra función inmitancia como una Z
dibujar_cauer_LC(k0, z_exc = F_cauer_0)


# Implementamos la función pero removiendo polos en el infinito
k0, F_cauer_0, rem = cauer_LC(FF, remover_en_inf=True)


# Tratamos a nuestra función inmitancia como una Z
dibujar_cauer_LC(k0, z_exc = F_cauer_0)