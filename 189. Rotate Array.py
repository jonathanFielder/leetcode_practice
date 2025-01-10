class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) > 1:
            nums2 = nums.copy()
            for i in range(len(nums)):
                nums[i] = nums2[(i - k) % len(nums)]
