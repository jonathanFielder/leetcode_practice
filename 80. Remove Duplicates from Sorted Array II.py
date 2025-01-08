class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(2, len(nums)):
            if nums[i - 1] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
