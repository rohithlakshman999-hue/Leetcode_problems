class Solution(object):
    def frequencySort(self, s):
        freq = [0] * 128

        for c in s:
            freq[ord(c)]+=1

        ans=[]
        for count in range(len(s),0,-1):
            for i in range(128):
                if(freq[i]==count):
                    ans.append(chr(i)*count)
        return ''.join(ans)

