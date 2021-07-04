#def differenceofSum(n. m)

#The function accepts two integers n, m as arguments 
# Find the sum of all numbers in range from 1 to m
# (both inclusive) that are not divisible by n. 
# Return difference between sum of integers not 
# divisible by n with sum of numbers divisible by n.

def differenceofSum(n,m):
    sum1 = 0
    sum2 = 0
    for i in range(len(m)):
        if i%n!=0:
            sum1 = sum1 + i
        else:
            sum2 = sum2 + i
    print(abs(sum2-sum1))             

n = int(input(""))
m = []