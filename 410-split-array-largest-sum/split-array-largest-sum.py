class Solution(object):
    def splitArray(self, arr, k):
        n=len(arr)
        l=max(arr)
        h=0
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
            if count<=k:
                h=mid-1
            else:
                l=mid+1
        return l
            