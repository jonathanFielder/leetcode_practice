class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        ret_list = []
        nums.sort()
        #print(nums)
        while i < len(nums) - 2:
            target = -nums[i]
            j = i + 1
            k  = len(nums) - 1
            while (j < k):
                summed = nums[j] + nums[k]
                if summed < target:
                    j += 1
                elif summed > target:
                    k -= 1
                else:
                    ret_list.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while(k > 0 and nums[k] == nums[k+1]):
                        k -= 1
            i += 1
            while(i < len(nums) - 1 and nums[i] == nums[i-1]):
                i += 1
        return ret_list
        
                
                
