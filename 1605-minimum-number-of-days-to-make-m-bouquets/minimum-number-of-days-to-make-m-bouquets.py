class Solution(object):
    def minDays(self, arr, m, k):
        n=len(arr)
        l=0
        h=max(arr)
        if m*k > n:
            return -1
            
        while(l<=h):
            mid=(l+h)//2
            s=0
            b=0
            for x in arr:
                if x <=mid:
                    s+=1
                else:
                    s=0
                if s==k:
                    b+=1
                    s=0
            if b>=m:
                h=mid-1
            else:
                l=mid+1
        return l