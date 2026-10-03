class Solution(object):
    def minEatingSpeed(self, arr, hi):
        n=len(arr)
        l=01
        h=max(arr)
        while(l<=h):
            mid=(l+h)//2
            hour=0
            for pile in arr:
                hour+=(pile+mid-1)//mid
            if hour<=hi:
                h=mid-1
            else:
                l=mid+1
        return l
        