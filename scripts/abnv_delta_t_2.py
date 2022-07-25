def timeDiff(t_2, t_1):
    h1, m1, s1 = t_1.split(':')
    h2, m2, s2 = t_2.split(':')
    diff = 3600*((int(h2)-int(h1))%24) + 60*(int(m2)-int(m1)) + (int(s2) - int(s1))

    return str(diff)

with open("delta_t", 'w') as diffs:
    with open("start_times") as f:
        previous_time = "0:0:0"
        first_iteration = True

        for line in f:
            current_time = line.strip().split()[2]
            #print(current_time)
            difference = timeDiff(current_time, previous_time)
            print(previous_time, current_time, difference)
            previous_time = current_time

            if not first_iteration:
                diffs.write(difference+'\n')

            first_iteration = False # skip the first loop
