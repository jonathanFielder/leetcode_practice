class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        ret = []
        z = 0
        for num in nums:
            if num:
                total *= num
            else:
                z += 1
        if z > 1:
            return [0] * len(nums)

        for num in nums:
            if z > 0:
                if num:
                    ret.append(0)
                else:
                    ret.append(total)
            else:
                ret.append(total // num)

        return ret
