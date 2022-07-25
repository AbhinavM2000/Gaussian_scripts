
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