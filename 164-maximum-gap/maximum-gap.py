class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        n=len(nums)
        x,maxi=0,0
        for i in range(1,n):
            x=nums[i]-nums[i-1]
            maxi=max(maxi,x)

        return maxi