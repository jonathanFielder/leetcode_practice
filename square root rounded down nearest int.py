import math

class Solution:
  def mySqrt(self, x: int) -> int:
    if x < 2:
      return x
    left = 0
    right = x//2
    mid = 0
    num = 0
    while(left <= right):
      mid = left + (right - left) // 2
      num = mid * mid
      if num > x:
        right = mid - 1
      elif num < x:
        left = mid + 1
      else:
        return mid
    return right
