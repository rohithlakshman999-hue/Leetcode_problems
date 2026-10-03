class Solution(object):
    def smallestDivisor(self, arr, t):
        n=len(arr)
        l=1
        h=max(arr)
        while(l<=h):
            mid=(l+h)//2
            s=0
            for x in arr:
                s+=(x+mid-1)//mid
            if s<=t:
                h=mid-1
            else: l=mid+1
        return l