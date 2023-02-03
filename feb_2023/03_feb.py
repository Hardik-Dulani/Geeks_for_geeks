# Given a binary matrix of dimensions with R rows and C columns.
# Start from cell(0, 0), moving in the right direction. Perform the following operations: 
# If the value of matrix[i][j] is 0, then traverse in the same direction and check the next value.
# If the value of matrix[i][j] is 1, then update matrix[i][j] to 0 and change the current direction clockwise.
# ie - up, right, down, or left directions change to right, down, left, and up respectively.
# Find the index of the cell where you will be forced to exit the matrix while performing the given traversal. 

def endPoints(self, matrix, R, C):
        def my_move(x,y,dirn):
            moves={"right":"down",
                "up":"right",
                "down":"left",
                "left":"up"
            }
            if matrix[x][y]==1:
                matrix[x][y]=0
                dirn = moves[dirn]
                
            if dirn=="right":
                y+=1
            elif dirn=="left":
                y-=1
            elif dirn=="down":
                x+=1
            else:
                x-=1
            return x,y,dirn
        dirn = "right"
        x,y=0,0
        while True:
            try:
                if matrix[x][y]==0 or matrix[x][y]==1:
                    if x<0 or y<0:
                        raise error
                    result_x,result_y=x,y
                    x,y,dirn = my_move(x,y,dirn)
            except:
                return result_x,result_y
