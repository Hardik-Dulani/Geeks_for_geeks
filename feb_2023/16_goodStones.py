# Geek is in a geekland which have a river and some stones in it.
# Initially geek can step on any stone.
# Each stone has a number on it representing the value of exact step geek can move.
# If the number is +ve then geeks can move right and if the number is -ve then geeks can move left.
# Bad Stones are defined as the stones in which if geeks steps, will reach a never ending loop 
# whereas good stones are the stones which are safe from never ending loops.
# Return the number of good stones in river.

def goodStones(self, n, arr):
    visited = [0]*n
    def dfs(i):

        nonlocal arr, visited, n
        if i < 0 or i >= n:
            return True

        if visited[i] > 0:
            return visited[i] == 2

        visited[i] = 1
        if dfs(i+arr[i]):
            visited[i] = 2
            return True
        return False

    return sum(dfs(i) for i in range(n))
