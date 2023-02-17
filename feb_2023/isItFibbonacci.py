# Geek just learned about Fibonacci numbers.

# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
# where the next number is found by adding up the two numbers before it.

# He defines a new series called Geeky numbers.
# Here the next number is the sum of the K preceding numbers.
# You are given an array of size K, GeekNum[ ],
# where the ith element of the array represents the ith Geeky number. Return its Nth term.

def kfibbo(N,K):
    geek_num += [0 for i in range(N-len(geek_num))]
    for i in range(k,N):
        geek_num[i] = sum(geek_num[i-k:i])
    return geek_num[N-1]
