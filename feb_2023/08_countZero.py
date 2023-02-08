# There are M job applicants and N jobs.  Each applicant has a subset of jobs that he/she is interested in.
# Each job opening can only accept one applicant and a job applicant can be appointed for only one job.
# Given a matrix G with M rows and N columns where G(i,j)
# denotes ith applicant is interested in the jth job. Find the maximum number of applicants who can get the job.




def countZero(self, n, k ,arr):
        res=[]
        mat_rows=set()
        mat_col=set()
        for i in arr:
            row,col=i
            mat_rows.add(row)
            mat_col.add(col)
            res.append((n-len(mat_rows))*(n-len(mat_col)))
        return res
