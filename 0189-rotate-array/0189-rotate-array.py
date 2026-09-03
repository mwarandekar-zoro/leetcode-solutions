class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        l = 0
        r = n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l = 0
        r = k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l = k
        r = n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
        