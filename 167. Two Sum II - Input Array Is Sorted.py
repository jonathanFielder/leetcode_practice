class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while (i < j):
            summed = numbers[i] + numbers[j]
            if summed < target:
                i += 1
            elif summed > target:
                j -= 1
            else:
                return [i+1, j+1]
        
