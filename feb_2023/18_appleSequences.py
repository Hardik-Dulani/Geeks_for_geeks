# There is a string of size n containing only 'A' and 'O'. 'A' stands for Apple, and
# 'O' stands for Orange. We have m number of spells, each spell allows us to convert an orange into an apple.

# Find the longest sequence of apples you can make, given a string and the value of m.


def appleSequences(self, n, m, arr):
     
    right,left = 0,0
    ans = 0
    while right < n:
        if arr[right] == 'A':
            right += 1
        elif m > 0:
            right += 1
            m -= 1
        else:
            ans = max(ans,right-left)
            while arr[left] != 'O':
                left += 1
            left += 1
            m += 1
    ans = max(ans,right-left)
    return ans
