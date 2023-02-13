# Given three integers  'A' denoting the first term of an arithmetic sequence ,
# 'C' denoting the common difference of an arithmetic sequence and an integer 'B'.
# you need to tell whether 'B' exists in the arithmetic sequence or not. 
# Return 1 if B is present in the sequence. Otherwise, returns 0.

def inSequence(self, A, B, C):
        if C==0:
            if A==B:
                return 1
            return 0
        res=((B-A)/C)+1
        if res>0 and res.is_integer():
            return 1
        return 0
