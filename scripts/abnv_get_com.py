
# Script that calculates COM for each structure, random and optimized

import numpy as np
i=0
arrays_opt = []
arrays_rand = []

with open("xyz_opt_str") as f:
    yourList = []
    for line in f:
        if line != '*\n':
            line = line.strip().split()
            line = [float(x) for x in line]
            yourList.append(line)

        else:
            yourArray = np.array(yourList)
            yourList = []
            arrays_opt.append(yourArray)

print(arrays_opt[0][:][:])                    #for the first opt str
print("length = ", len(arrays_opt))

print("\n")

with open("xyz_rnd_str") as f2:
    yourList2 = []
    for line in f2:
        if line != '*\n':
            line = line.strip().split()
            line = [float(x) for x in line]
            yourList2.append(line)

        else:
            yourArray2 = np.array(yourList2)
            yourList2 = []
            arrays_rand.append(yourArray2)

print(arrays_rand[0][:][:])                     #for the first rand str
print("length = ", len(arrays_rand))

while i < len(arrays_rand):
    print("Str "+ str(i+1))
    print("-------")
    print("Rand")
    print('Rx = '+str(sum(arrays_rand[i][:,0]*arrays_rand[i][:,3])/sum(arrays_rand[i][:,3])))
    print('Ry = '+str(sum(arrays_rand[i][:,1]*arrays_rand[i][:,3])/sum(arrays_rand[i][:,3])))
    print('Rz = '+str(sum(arrays_rand[i][:,2]*arrays_rand[i][:,3])/sum(arrays_rand[i][:,3])))
    
    print("Opt")
    print('Rx = '+str(sum(arrays_opt[i][:,0]*arrays_opt[i][:,3])/sum(arrays_opt[i][:,3])))
    print('Ry = '+str(sum(arrays_opt[i][:,1]*arrays_opt[i][:,3])/sum(arrays_opt[i][:,3])))
    print('Rz = '+str(sum(arrays_opt[i][:,2]*arrays_opt[i][:,3])/sum(arrays_opt[i][:,3])))
    print("\n")
    i=i+1