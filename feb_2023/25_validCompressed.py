# A special compression mechanism can arbitrarily delete 0 or more characters and replace them with the deleted character count.
# Given two strings, S and T where S is a normal string and T is a compressed string, 
# determine if the compressed string  T is valid for the plaintext string S. 

def checkCompressed( s,t):
    i=0
    j=0

    slen=len(s)
    tlen=len(t)

    while i<slen and j<tlen:
        # print(i,j)
        if s[i]==t[j]:
            i+=1
            j+=1
        elif t[j].isdigit():
            num=0
            while j<tlen and t[j].isdigit():
                c=int(t[j])
                num=num*10+c
                j+=1
            i=i+num

        else:
            return 0

    if i==slen and j==tlen:
        return 1
    else:
        return 0
