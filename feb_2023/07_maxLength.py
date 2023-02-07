# Given an array arr[] consisting of n integers, 
# find the length of the longest subarray with positive (non zero) product.

from numpy import prod

def maxLength(arr,n):


    total = []
    for j in range(n):
        pros = [(arr[j:i+1]) for i in range(j,n) ]
        total.append(pros)
    new = []
    for i in total:
        for j in i:
            new.append(j) 
    my = [len(x) for x in new if prod(x)>0]
    if my==[]:
        return 0
    return (max(my))
    
