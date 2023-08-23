#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:38:55 2021

@author: mariano

Matriz Admitancia Indefinida (MAI)
----------------------------------
Ejemplos de cálculo simbólico mediante MAI de una red T puenteada de R constante.

Referencias:
------------
Cap. 9. Avendaño L. Sistemas electrónicos Analógicos: Un enfoque matricial.
"""

import sympy as sp

from pytc2.cuadripolos import calc_MAI_vtransf_ij_mn
from pytc2.general import print_latex


# T puenteado cargado: red de R constante
# explicación:
'''    
+ Numeramos los polos de 0 a n=3

    0-------+--L1----2---L3---1
                     |       |
                    C2       G
                    |       |
    3--------------+--------
    
'''    

## Definición de las variables simbólicas
s = sp.symbols('s', complex=True)
L1, C2, L3, G = sp.symbols('L1 C2 L3 G', real=True, positive=True)

## Armo la MAI

##              Nodos: 0            1              2               3
Ymai = sp.Matrix([  
                    [ 1/(s*L1),       0,              -1/(s*L1),                  0    ],
                    [     0,      1/(s*L3) + G,       -1/(s*L3),                 -G    ],
                    [ -1/(s*L1),   -1/(s*L3) ,   s*C2 + 1/(s*L3) + 1/(s*L1),    -s*C2  ],
                    [     0,           -G,              -s*C2,                G + s*C2 ]
                 ])
print_latex(sp.latex(Ymai))

con_detalles = False
# con_detalles = True

Vmai = calc_MAI_vtransf_ij_mn( Ymai, 1, 3, 0, 3, verbose=con_detalles)


print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(3, 1, 0, 1) +  sp.latex(Vmai))


