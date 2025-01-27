class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            small = min(height[i], height[j])
            volume = small * (j - i)
            if volume > largest:
                largest = volume
            if height[i] == small:
                i += 1
            else:
                j -= 1
        return largest
