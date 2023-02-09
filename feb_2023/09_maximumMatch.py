# There are M job applicants and N jobs.  
# Each applicant has a subset of jobs that he/she is interested in. 
# Each job opening can only accept one applicant and a job applicant can be appointed for only one job. 
# Given a matrix G with M rows and N columns where G(i,j) denotes ith applicant is interested in the jth job. 
# Find the maximum number of applicants who can get the job.


def maximumMatch(self,G):

        m, n = len(G), len(G[0])

        match = [-1] * n

        visited = [False] * n

        def dfs(i):

            for j in range(n):

                if G[i][j] and not visited[j]:

                    visited[j] = True

                    if match[j] == -1 or dfs(match[j]):

                        match[j] = i

                        return True

            return False

        count = 0

        for i in range(m):

            visited = [False] * n

            if dfs(i):

                count += 1

        return count
