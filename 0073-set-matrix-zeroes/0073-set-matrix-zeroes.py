class Solution(object):
    def setZeroes(self, arr):
        n=len(arr)
        m=len(arr[0])
        rows=[]
        col=[]
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    rows.append(i)
                    col.append(j)

        for i in rows:
            for j in range (m):
                arr[i][j]=0
        for j in col:
            for i in range(n):
                arr[i][j]=0
        return arr