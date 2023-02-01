# 1.02.2023
# There is a row of N houses, each house can be painted with one of the three colors: red, blue or green
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color. 
# Find the minimum cost to paint all houses.
# The cost of painting each house in red, blue or green colour is given in the array r[], g[] and b[] respectively.



def distinctColoring (N, r, g, b):
    arr = [r, g, b]
        
    for i in range(N-2, -1, -1):
        arr[0][i] += min(arr[1][i+1], arr[2][i+1])
        arr[1][i] += min(arr[0][i+1], arr[2][i+1])
        arr[2][i] += min(arr[1][i+1], arr[0][i+1])

    return min(arr[0][0], arr[1][0], arr[2][0])
