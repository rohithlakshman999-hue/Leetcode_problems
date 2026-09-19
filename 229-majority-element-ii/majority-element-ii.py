class Solution(object):
    def majorityElement(self, arr):
        freq={}
        ans=[]
        for x in arr:
            freq[x]=freq.get(x,0)+1
        for x in freq:
            if freq[x] > len(arr)//3:
                ans.append(x)
        return ans