
#Extracts position block of random and optimized for abnv_get_xyzm.py | Note : Last entry (BFGS 0 to BFGS X) will be ignored |

import linecache as lc

with open("bh.py.out") as big_file:  # scan file to find the positions
    BFGS_Zero_lno = []
    pos_BFGS_Zero_lno = []
    pos_rnd_str_lno = []

    isAfterZero = False

    prevNum = -1

    for num, string in enumerate(big_file):
        if string.startswith("Positions:"):

            if isAfterZero:
                pos_BFGS_Zero_lno.append(num + 1)
                isAfterZero = False

            prevNum = num

        if string.startswith("BFGS:    0"):
            BFGS_Zero_lno.append(num + 1)
            isAfterZero = True

            if len(BFGS_Zero_lno) > 1:
                pos_rnd_str_lno.append(prevNum + 1)

#### read positions and write to resp. files ####
with open("start_times", 'w') as BFGSzeroFile:
    for num in BFGS_Zero_lno:
        line = lc.getline("bh.py.out", num)
        BFGSzeroFile.write(line)

with open("pos_Rand_structures", 'w') as posRndFile:
    for num in pos_BFGS_Zero_lno:
        for i in range(1, 15):
            line = lc.getline("bh.py.out", num + i)
            posRndFile.write(line)
        posRndFile.write("***\n")

with open("pos_Opt_structures", 'w') as posOptFile: #still misses last optimised str, misses copying , deleted last rand,opt str set to fix, actually delted the rand, bc opt was unavailable. #here
    for num in pos_rnd_str_lno:
        for i in range(1, 15):
            line = lc.getline("bh.py.out", num + i)
            posOptFile.write(line)
        posOptFile.write("***\n")

with open('pos_Rand_structures') as f1: #here
    lines = f1.readlines()

with open('pos_Rand_structures', 'w') as f2: #here
    f2.writelines(lines[:-15])
    
times=[]    
    
    
    
    #Calcuation of time interval
    
#with open("start_times") as time_file:
#    for string2 in time_file:
#             string2 = string2.strip().split()
#             times.append(string2)
#print(times[3])