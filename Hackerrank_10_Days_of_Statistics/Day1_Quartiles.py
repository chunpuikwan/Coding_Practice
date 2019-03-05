# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import statistics

size = int(input())
array = list(map(int, input().split()))

array.sort()
mid = int(len(array)/2)

#print(array[:mid])
if size % 2 == 0:
    #Even case
    first_Quart = statistics.median(array[:mid])
    third_Quart = statistics.median(array[mid:])
else:
    #Odd case
    first_Quart = statistics.median(array[:mid])
    third_Quart = statistics.median(array[mid+1:])

print(int(first_Quart))
print(int(statistics.median(array)))
print(int(third_Quart))

