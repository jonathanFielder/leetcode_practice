class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = 0
        c = 0
        n_div  = len(nums) // 2
        for i in nums:
            if c == 0:
                m = i
                c += 1
            elif i != m:
                c -= 1
            else: c += 1
            if c > n_div:
                return m
        return m

                
        
