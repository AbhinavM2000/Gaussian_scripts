
#Allocates mass to atoms and obtains [x y z m] format for random and optimized for abnv_get_com.py

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