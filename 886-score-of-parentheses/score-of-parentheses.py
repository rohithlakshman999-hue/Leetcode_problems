class Solution(object):
    def scoreOfParentheses(self, s):
        score=0
        c=0
        for i in range(len(s)):
            if s[i]=='(':
                c+=1
            elif s[i] == ')':
                c-=1
                if s[i-1]=='(':
                    score += 2**c
        return score
        