# Given an array Arr of size N containing positive integers. 
# Find the maximum sum of a subsequence such that
# no two numbers in the sequence should be adjacent in the array.


def findMaxSum(self,arr, n):
        a = 0
        b = 0
        for i in range(1,n+1):
            temp=a
            a=max(a,b)
            b=temp+arr[i-1]
      
      
        return max(a,b)
