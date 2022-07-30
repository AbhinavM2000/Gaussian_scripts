"""
Script to calculate corelation parameter
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


import math
import numpy as np
BigArrayX = []
BigArrayY = []

xx=open("ZnO_rand_767.txt", 'r')
yy=open("time_767.txt", 'r')
n=767

for line in xx:
    xcord = float(line)
    ycord = float(yy.readline())
    ValuesX = np.array([xcord])
    BigArrayX.append(ValuesX)
    ValuesY = np.array([ycord])
    BigArrayY.append(ValuesY)
    
#X_coord = BigArrayX
#Y_coord = BigArrayY



#BigArrayX = []
#BigArrayY = []

#BigArrayX = [1,2,3,4,5,6,7,8,9,10]
#BigArrayY = [200,-67,17,116,-25,0,0.49,6.4,-81,10000]

BigArrayX = np.array(BigArrayX)
BigArrayY = np.array(BigArrayY)

rnr = n*(sum(abs(BigArrayX*BigArrayY))) - (sum(abs(BigArrayX)))*(sum(abs(BigArrayY)))
dnr = math.sqrt((n*(sum(abs(BigArrayX*BigArrayX))) - (sum(abs(BigArrayX)))*(sum(abs(BigArrayX))))*( n*(sum(abs(BigArrayY*BigArrayY))) - (sum(abs(BigArrayY)))*(sum(abs(BigArrayY)))))

print(rnr/dnr)