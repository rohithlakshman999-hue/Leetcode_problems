class Solution(object):
    def subsets(self, arr):
        ans=[[]]

        for x in arr:
            new=[]
            for old in ans:
                new.append(old+[x])
            ans+=new

        return ans