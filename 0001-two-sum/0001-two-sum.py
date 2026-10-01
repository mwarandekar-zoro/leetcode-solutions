class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        seen = {}
        for i in range(n):
            num = nums[i]
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i


        