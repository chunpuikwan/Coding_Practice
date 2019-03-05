# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

no_of_numbers = int(input())
numbers = list(map(int, input().split()))
frequency = list(map(int, input().split()))

S = []

for i in range(no_of_numbers):                 #Taken from discussion
    S += [numbers[i]]*frequency[i]             #Taken from discussion

mid = int(len(S)/2)
S.sort()

if int(len(S)) % 2 == 0:
    #Even case
    first_Quart = statistics.median(S[:mid])
    third_Quart = statistics.median(S[mid:])
else:
    #Odd case
    first_Quart = statistics.median(S[:mid])
    third_Quart = statistics.median(S[mid+1:])

print(format(third_Quart - first_Quart, '.1f'))

#print(numbers)
#print(frequency)
