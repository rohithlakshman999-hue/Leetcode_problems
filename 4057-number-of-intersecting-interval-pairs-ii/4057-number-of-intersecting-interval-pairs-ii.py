class Solution(object):
    def countIntersectingIntervals(self, arr):
        start=[]
        end=[]

        for x in arr:
            start.append(x[0])
            end.append(x[1])

        start.sort()
        end.sort()
        count=0
        j=0
        for i in range(len(start)):
            while j<len(end) and end[j]<start[i]:
                j+=1
            count+=i-j
        return count