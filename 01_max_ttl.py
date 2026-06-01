# To find the maximum ttl value and the input log can be given in cli 
# 1. run 
# 2. paste the logs 
# 3. ctrl+z enter 
# 4. output 255 will be printed

import sys
max_ttl=-1
data = sys.stdin.read()
#     # process each line
for line in data:   #data = sys.stdin.read()
#     # process each line
#     print(line.strip())

#with open("input.txt", "r") as f:
# for line in f:
        line = line.strip()
        #print(line)
        parts=line.split()
        for part in parts:
            if part.startswith("ttl="):
                ttl=int(part.split("=")[1])
                if ttl>=max_ttl:
                    max_ttl=ttl
print(max_ttl)



