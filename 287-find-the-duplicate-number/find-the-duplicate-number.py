class Solution(object):
    def findDuplicate(self, arr):
        n=len(arr)
        l=0
        h=n-1
        while(l<=h):
            mid=(l+h)//2
            count=0
            for x in arr:
                if x<=mid:
                    count+=1
            if count>mid:
                h=mid-1
            else:
                l=mid+1
        return l


        