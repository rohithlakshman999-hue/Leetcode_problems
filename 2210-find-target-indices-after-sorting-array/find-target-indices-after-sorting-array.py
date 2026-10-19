class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        n=len(nums)
        arr=[]
        for i in range(n):
            if nums[i]==target:
                arr.append(i)
        return arr
        