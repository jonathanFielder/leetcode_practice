class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        print('nums1', nums1)
        print('nums2', nums2)
        if n < 1:
            return
        for i in range(m):
            print('nums1', nums1)
            print('nums2', nums2)
            print('compare', nums1[i], nums2[0])
            if nums2[0] < nums1[i]:
                temp = nums1[i]
                nums1[i] = nums2[0]
                nums2[0] = temp
                curr = 1
                if curr < n:
                    while nums2[curr - 1] > nums2[curr]:
                        t = nums2[curr - 1]
                        nums2[curr - 1] = nums2[curr]
                        nums2[curr] = temp
                        curr += 1
                        if not curr < n:
                            break
        for j in range(n):
            print('second loop')
            print('nums1', nums1)
            print('nums2', nums2)
            nums1[m + j] = nums2[j]

        
