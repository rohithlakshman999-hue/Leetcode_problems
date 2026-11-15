class Solution(object):
    def countConsistent(self, nums):
        n=len(nums)
        count=0
        for i in range(n):
            mini=nums[i]
            and_val=nums[i]
            for j in range(i,n):
                mini=min(mini,nums[j])
                and_val=and_val&nums[j]
                if mini==and_val:
                    count+=1
        return count