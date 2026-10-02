class Solution(object):
    def findMin(self, arr):
        n=len(arr)
        l=0
        h=n-1
        ans = float('inf')
        while(l<=h):
            mid=(l+h)//2
            if(arr[l]<=arr[mid]):
                ans=min(ans,arr[l])
                l=mid+1
            else:
                ans=min(ans,arr[mid])
                h=mid-1
        return ans
        