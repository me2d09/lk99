# -*- coding: utf-8 -*-
"""weighting.ipynb
"""

!pip install periodictable

from periodictable import formula
f = formula("Cu3P")
mass = 15   # mass in g
for k,v in f.mass_fraction.items():
  print(f"{str(k) : >2}{v*mass:9.4f}g")