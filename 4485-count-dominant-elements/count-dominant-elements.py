class Solution(object):
    def countDominantElements(self, nums):
        n = len(nums)
        count = 0

        if n == 1:
            return 1

        for i in range(n):
            if i == 0:
                if nums[i] >= nums[i + 1]:
                    count += 1

            elif i == n - 1:
                if nums[i] >= nums[i - 1]:
                    count += 1

            else:
                if 2 * nums[i] >= nums[i - 1] + nums[i + 1]:
                    count += 1

        return count