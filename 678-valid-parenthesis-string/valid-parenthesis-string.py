class Solution(object):
    def checkValidString(self, s):
        count=0
        count1=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                count1+=1
            elif s[i]==")":
                count-=1
                count1-=1
            else:
                count-=1
                count1+=1
            if count1<0:
                return False
            if count<0:
                count=0
        
        return count==0
            