class Solution(object):
    def shipWithinDays(self, arr, d):
        n=len(arr)
        l=0
        h=0
        l=max(arr)
        for x in arr:
            h+=x
        while(l<=h):
            mid=(l+h)//2
            sum=0
            count=1
            for x in arr:
                if sum+x<=mid:
                    sum+=x
                else:
                    count+=1
                    sum=x

            if count<=d:
                h=mid-1
            else:
                l=mid+1
        return l