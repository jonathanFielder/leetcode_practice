class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tally = {}
        n_div  = len(nums) / 2
        for i in nums:
            if i in tally:
                tally[i] += 1
            else:
                tally[i] = 1
            if tally[i] > n_div:
                    return i

                
        
        
