class Solution(object):
    def removeKdigits(self, num, k):
        res=[]
        for x in num:
            while res and k>0 and res[-1]>x:
                res.pop()
                k-=1
            res.append(x)
        while res and k>0:
            res.pop()
            k-=1
        ans=''.join(res).lstrip('0')
        return ans if ans else "0"
