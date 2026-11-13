class Solution(object):
    def merge(self, arr):
        arr.sort()
        n=len(arr)
        ans=[]
        start=arr[0][0]
        end=arr[0][1]
        for i in range(1,n):
            if(arr[i][0]<=end):
                end=max(end,arr[i][1])
            else:
                ans.append([start,end])

                start=arr[i][0]
                end=arr[i][1]

        ans.append([start,end])
        return ans