# You are given the head of a linked list.
# You have to replace all the values of the nodes with the nearest prime number.
# If more than one prime number exists at an equal distance, choose the smallest one.

from typing import Optional


def sieve(x, y):
    # create a list of all the numbers in the range
    numbers = [i for i in range(x, y+1)]
     
    # start with the first number in the list
    i = 0
     
    # loop until we reach the end of the list
    while i < len(numbers):
        # if the current number is not already crossed out,
        # cross out all of its multiples
        if numbers[i] is not None:
            for j in range(i+numbers[i], len(numbers), numbers[i]):
                numbers[j] = None
        i += 1
     
    # return the list of prime numbers
    return [n for n in numbers if n is not None]
def give(l,x):
    m = 0
    n = len(l)
    p = 0
    lp=-1
    while(lp!=p):
        lp=p
        p = (m+n)//2
        if(l[p]==x):
            return [p,True]
        if(l[p]>x):
            n = p
        if(l[p]<x):
            m = p
    return [p,False]
        

class Solution:
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        k = -1
        p = head
        while(p!=None):
            if(p.data>k):
                k = p.data
            p = p.next
     
        t = sieve(2,2*k+1)
        o = head
        while(o!=None):
            a,b = give(t,o.data)
            if(b==False):
                d = o.data - t[a]
                e = t[a+1] - o.data
                if(d<=e):
                    o.data = t[a]
                else:
                    o.data = t[a+1]
            o = o.next
        return head
