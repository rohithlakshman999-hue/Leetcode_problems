class Solution(object):
    def searchMatrix(self, mat, t):
        n=len(mat)
        m=len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j]==t:
                    return True 
        return False
        