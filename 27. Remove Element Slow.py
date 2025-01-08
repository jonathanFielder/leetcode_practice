class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        print('init',nums)
        print('val',val)
        if p1 == p2:
            if nums[p1] == val:
                return 0
            else:
                return 1
        if len(nums) == 0:
            return 0
        while p1 < p2:
            if nums[p1] == val:
                while nums[p2] == val:
                    p2 -= 1
                    if p2 == 0:
                        if nums[p2] == val:
                            return 0
                        else:
                            return 1
                if p2 > p1:
                    nums[p1] = nums[p2]
                    p2 -= 1
            p1 += 1
            print(nums)
        while nums[p2] == val:
            p2 -= 1
            if p2 == 0:
                if nums[p2] == val:
                    return 0
                else:
                    return 1
        return p2 + 1
        
