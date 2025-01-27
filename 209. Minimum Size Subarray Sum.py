class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        shortest = len(nums) + 1
        summed = nums[i]
        while i <= j and j < len(nums):
            if summed < target:
                j += 1
                if j < len(nums):
                    summed += nums[j]
            else:
                if j - i < shortest:
                    shortest = j - i + 1
                summed -= nums[i]
                i += 1
        if shortest == len(nums) + 1:
            shortest = 0
        return shortest
        
