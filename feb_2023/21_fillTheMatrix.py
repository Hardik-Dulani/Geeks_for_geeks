# Given a matrix with dimensions N x M, 
# entirely filled with zeroes except for one position at co-ordinates X and Y containing '1'. 
# Find the minimum number of iterations in which the whole matrix can be filled with ones.
# Note: In one iteration, '1' can be filled in the 4 neighbouring elements of a cell containing '1'.

def minIteration(N, M, x, y):
    if(N==1 and M==1):
        return 0
    s=0
    r=0
    if(y >(M-y)):
        s= y-1
    else:
        s= M-y
    if(x >(N-x)):
        r= x-1
    else:
        r= N-x
    return s+r
