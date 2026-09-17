class Solution(object):
    def rearrangeArray(self, arr):
        n=len(arr)
        p=[]
        ne=[]
        for i in range(n):
            if(arr[i]<0):
                ne.append(arr[i])
            else:
                p.append(arr[i])
        res=[]
        for i in range(n/2):
            res.append(p[i])
            res.append(ne[i])
        return res        