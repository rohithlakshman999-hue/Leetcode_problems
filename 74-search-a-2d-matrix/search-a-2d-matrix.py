class Solution(object):
    def searchMatrix(self, mat, t):
        n=len(mat)
        m=len(mat[0])
        i=0
        j=(n*m)-1
        while(i<=j):
            mid = i+(j-i)//2
            if(mat[mid//m][mid%m]==t):
                return True
            if (mat[mid//m][mid%m]<t):
                i=mid+1
            else:
                j=mid-1
        return False