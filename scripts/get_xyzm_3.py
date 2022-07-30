"""
Allocates mass to atoms and obtains [x y z m] format for random and optimized for abnv_get_com.py
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

import numpy
from scipy import ndimage

xyzOptstr = open("xyz_opt_str", 'w')

xyzm = numpy.array([])
with open('pos_Opt_structures') as infile:
    i = 0
    k = 0
    j = [65.38, 65.38, 65.38, 65.38, 15.999, 15.999, 15.999, 15.999, 1.00784, 1.00784, 1.00784, 1.00784, 15.999,
         1.00784, -1]
    for line in infile:
        try:
            if j[k] == -1:
                k = 0
            mass = str(j[k])
            k = k + 1
            xxx = line.split()[2] + ' ' + line.split()[3] + ' ' + line.split()[4] + ' ' + mass + ' \n'
            xyzOptstr.write(str(xxx))
            i = i + 1
        except IndexError:
            xyzOptstr.write("*\n")
            pass
        continue
print(i)

xyzOptrnd = open("xyz_rnd_str", 'w')
with open('pos_Rand_structures') as infile2:
    i = 0
    k = 0
    j = [65.38, 65.38, 65.38, 65.38, 15.999, 15.999, 15.999, 15.999, 1.00784, 1.00784, 1.00784, 1.00784, 15.999,
         1.00784, -1]
    for line in infile2:
        try:
            if j[k] == -1:
                k = 0
            mass = str(j[k])
            k = k + 1
            xxx = line.split()[2] + ' ' + line.split()[3] + ' ' + line.split()[4] + ' ' + mass + ' \n'
            xyzOptrnd.write(str(xxx))
            i = i + 1
        except IndexError:
            xyzOptrnd.write("*\n")
            pass
        continue