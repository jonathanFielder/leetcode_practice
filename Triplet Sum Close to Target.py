import math

class Solution:
  def searchTriplet(self, arr, target_sum):
    arr.sort()
    trav = 0
    left = trav + 1
    right = len(arr) - 1
    closest = arr[trav] + arr[left] + arr[right]
    for trav in range(len(arr) - 2):
      left = trav + 1
      right = len(arr) - 1
      while left < right:
        added = arr[trav] + arr[left] + arr[right]
        if added == target_sum:
          return added
        if abs(target_sum - added) < abs(target_sum - closest):
          closest = added
        elif abs(target_sum - added) == abs(target_sum - closest):
          if added < closest:
            closest = added
        if added < target_sum:
          left += 1
        else:
          right -= 1
    return closest
