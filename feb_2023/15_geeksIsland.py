# Geeks Island is represented by an N * M matrix mat. 
# The island is touched by the Indian Ocean from the top and left edges and the Arabian Sea from the right and bottom edges.
# Each element of the matrix represents the height of the cell.
# Due to the rainy season, the island receives a lot of rainfall, 
# and the water can flow in four directions(up, down, left, or right) 
# from one cell to another one with height equal or lower.
# You need to find the number of cells from where water can flow to both the Indian Ocean and the Arabian Sea.

#User function Template for python3

from collections import deque
class Solution():
    def water_flow(self, mat, n, m):
        #your code goes here
        output = 0
        q = deque()
        v1 = set()
        for i in range(1,len(mat[0])):
            q.append([0,i])
            v1.add((0,i))
        for i in range(len(mat)):
            q.append([i,0])
            v1.add((i,0))
        
        while len(q) != 0:
            a,b = q.popleft()
            for i,j in [[a,b+1],[a+1,b],[a,b-1],[a-1,b]]:
                if 0<=i<len(mat) and 0<=j<len(mat[0]) and mat[i][j] >= mat[a][b] and (i,j) not in v1 :
                    v1.add((i,j))
                    q.append([i,j])
        v2 = set()
        for i in range(len(mat[0])-1):
            q.append([len(mat)-1,i])
            v2.add((len(mat)-1,i))
        for i in range(len(mat)):
            q.append([i,len(mat[0])-1])
            v2.add((i,len(mat[0])-1))
        while len(q) != 0:
            a,b = q.popleft()
            if (a,b) in v1: 
                # print(a,b)
                output += 1
            for i,j in [[a,b+1],[a+1,b],[a,b-1],[a-1,b]]:
                if 0<=i<len(mat) and 0<=j<len(mat[0]) and mat[i][j] >= mat[a][b] and (i,j) not in v2 :
                    v2.add((i,j))
                    q.append([i,j])
        return output
        


