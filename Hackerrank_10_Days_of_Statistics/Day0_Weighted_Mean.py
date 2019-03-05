# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

size = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

dot_product = 0

for i,j in zip(numbers, weights):
    dot_product += i*j

denominator = sum(weights)
print(format(dot_product/denominator, '.1f'))
