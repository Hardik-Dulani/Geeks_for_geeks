# Given a maze with N cells.
# Each cell may have multiple entry points but not more than one exit
# (i.e entry/exit points are unidirectional doors like valves).
# You are given an array Edge[] of N integers,
# where Edge[i] contains the cell number that can be reached from of cell i in one step.
# Edge[i] is -1 if the ith cell doesn't have an exit. 
# The task is to find the largest sum of a cycle in the maze
# (Sum of a cycle is the sum of the cell indexes of all cells present in that cycle).
# Note:The cells are named with an integer value from 0 to N-1. If there is no cycle in the graph then return -1.

def largestSumCycle(N, Edge):
        arrays=[]
        for i in range(N):
            total,my_var= [],[]
            for k in range(i,N):
                if Edge[i]==-1:
                    break
                else:
                    total.append(i)
                    i=Edge[i]
                    if i in total:
                        my_var = total[total.index(i):]
                        break
            if len(my_var)>1 and sum(my_var) not in arrays:
                arrays.append(sum(my_var))
        if len(arrays)>0:
            result= max(arrays)
            return result
        return-1
