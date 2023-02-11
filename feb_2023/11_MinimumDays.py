# Given a string S of length N containing only lowercase alphabets.
# You are also given a permutation P of length N containing integers from 0 to N-1. 
# In (i+1)'th day you can take the P[i] value of the permutation array and replace S[P[i]] with a '?'.

# You have to tell the minimum number of days required, 
# such that after it for all index i (0<=i<N-1), if S[i]!='?', then S[i]!=S[i+1].

def getMinimumDays(N,S,P):
        dic={d:i+1 for i,d in enumerate(P)}
        result=0
        for i in range(N-1):
            if S[i]==S[i+1]:
                x=dic[i]
                y=dic[i+1]
                
                result=max(result,min(x,y))
                
        return result
