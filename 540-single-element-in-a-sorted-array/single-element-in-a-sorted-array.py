class Solution(object):
    def singleNonDuplicate(self, nums):
        freq=[0]*1000000
        for i in range(len(nums)):
            freq[nums[i]]+=1


        for i in range(len(freq)):
            if freq[i]==1:
                return i
        return 0
        