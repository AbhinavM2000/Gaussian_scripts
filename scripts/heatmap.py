"""
Heatmap plot script
Copyright (C) 2022  Abhinav M

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
randname=input()
optname=input()
timename=input()
xx=open(randname, 'r')
yy=open(optname, 'r')
tt=open(timename, 'r')
BigArrayX = []
BigArrayY = []
BigArrayT = []
x_lab=input()
y_lab=input()
clblabel=input()
for line in xx:
    xcord = float(line)
    ycord = float(yy.readline())
    tcord = float(tt.readline())
    ValuesX = np.array([xcord])
    BigArrayX.append(ValuesX)
    
    ValuesY = np.array([ycord])
    BigArrayY.append(ValuesY)
    
    ValuesT = np.array([tcord])
    BigArrayT.append(ValuesT)
X_coord = BigArrayX
Y_coord = BigArrayY
Z_coord = BigArrayT

# Generate data...
x = np.random.random(10)
y = np.random.random(10)
plt.xlabel(x_lab)
plt.ylabel(y_lab)
# Plot...
plt.scatter(X_coord, Y_coord, c=Z_coord, s=75,cmap='jet',alpha=0.5,edgecolors='none')
#plt.colorbar()
clb = plt.colorbar()
clb.set_label(clblabel)
plt.show()