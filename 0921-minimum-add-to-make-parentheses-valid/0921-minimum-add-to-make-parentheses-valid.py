class Solution(object):
    def minAddToMakeValid(self, s):
        n=len(s)
        count=0
        ans=0
        for i in range(n):
            if s[i]=='(':
                count+=1
            else:
                if count>0:
                    count-=1
                else:
                    ans+=1
        return count+ans