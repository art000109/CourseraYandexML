import os
import os.path
n = int(input())
for i in range(1,n+1):
    if os.path.exists(f'Week {i}'):
        continue
    os.mkdir(f'Week {i}')
