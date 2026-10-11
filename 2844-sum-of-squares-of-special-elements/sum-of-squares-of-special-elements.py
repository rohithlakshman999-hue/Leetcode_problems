class Solution(object):
    def sumOfSquares(self, nums):
        sum=0
        n=len(nums)
        for i in range(len(nums)):
            if n%(i+1)==0:
                sum+=(nums[i]*nums[i])
        return sum

        