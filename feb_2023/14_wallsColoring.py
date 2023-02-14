# There is a row of N walls in Geeksland.
# The king of Geeksland ordered Alexa to color all the walls on the occasion of New Year.
# Alexa can color each wall with either pink, black, or yellow.
# The cost associated with coloring each wall with a particular color is represented by a 2D array colors of size N*3 ,
# where colors[i][0], colors[i][1], and colors[i][2] is the cost
# of painting ith wall with colors pink, black, and yellow respectively.
# You need to find the minimum cost to color all the walls such that no two adjacent walls have the same color.


def minCost(self, arr, N):
        for i in range(N-2, -1, -1):
            arr[i][0] += min(arr[i+1][1], arr[i+1][2])
            arr[i][1] += min(arr[i+1][0], arr[i+1][2])
            arr[i][2] += min(arr[i+1][1], arr[i+1][0])
    
        return min(arr[0][0], arr[0][1], arr[0][2])
