class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        m -= 1
        n -= 1
        for put in range(len(nums1) - 1, -1, -1):
            if n >= 0 and m >= 0:
                if nums1[m] > nums2[n]:
                    nums1[put] = nums1[m]
                    m -= 1
                else:
                    nums1[put] = nums2[n]
                    n -= 1
            elif n >= 0:
                nums1[put] = nums2[n]
                n -= 1

        
