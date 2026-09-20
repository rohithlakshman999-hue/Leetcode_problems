class Solution(object):
    def countIntersectingIntervals(self, arr):
        n=len(arr)
        n1=len(arr[0])
        count=0

        for i in range(n):
            for j in range(i+1,n):
                if arr[i][0]<=arr[j][1] and arr[j][0]<=arr[i][1]:
                    count+=1
        return count
                    