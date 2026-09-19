class Solution(object):
    def subarraySum(self, arr, k):
        n=len(arr)
        freq={0:1}
        sum=0
        count=0
        for x in arr:
            sum+=x
            if sum-k in freq:
                count+=freq[sum-k]
            freq[sum]=freq.get(sum,0)+1
        return count