#input
# 2026-05-27 10:15:20 - Login success
# 2026-05-27 11:45:10 - File uploaded
# 2026-05-27 10:30:10 - updated settings
# 2026-05-28 09:00:00 - System reboot
# 2026-05-28 10:30:30 - User logout

# output

# Date: 2026-05-27
#   Login success
#   File uploaded

# Date: 2026-05-28
#   System reboot
#   User logout


with open("input1.txt", "r") as f:
    data = f.read().strip().split('\n')
    #print(data)
    #print(f)

    logs = []

# remove empty lines
    for line in data:
        line = line.strip()
        if line != "":
            logs.append(line)
    #print (logs)

    #convert hours to minutes (not used in this code)
    # def get_minutes(ts):
    #     time = ts.split()[1]
    #     h, m, s = time.split(':')
    #     return int(h) * 60 + int(m)






    group = []
    result = []

    for i in range(len(logs)):
        if i == 0:
            #print(logs[i])
            group.append(logs[i])
            #print(group)
            continue

        prev_date = logs[i-1].split()[0]
        #print(prev_date)
        curr_date = logs[i].split()[0]

        if prev_date == curr_date:
            group.append(logs[i])
        else:
            result.append(group)
            #print(logs[i])
            group = [logs[i]] #start new group
            #print(group)

    result.append(group)
    # print(result)


    for i, g in enumerate(result, 1):
        print("Day", i)
        #print(g)
        for line in g:
            print(line)
    
    
    # i = 1
    # for g in result:
    #     print("Day", i)
    #     print(g)
    #     for line in g:
    #         print(line)
    #     i += 1

