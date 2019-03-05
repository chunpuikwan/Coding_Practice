# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))

print(np.around(np.mean(numbers), decimals=1))
print(np.around(np.median(numbers),decimals=1))
mode = stats.mode(numbers)
print(mode[0][0])
