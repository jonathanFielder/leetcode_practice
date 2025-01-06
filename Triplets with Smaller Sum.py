class Solution:
  def searchTriplets(self, arr, target):
    count = 0
    arr.sort()
    trav = 0
    for trav in range(len(arr) - 2):
      for left in range(trav + 1, len(arr) - 1):
        right = left + 1
        while arr[trav] + arr[left] + arr[right] < target and right < len(arr):
          summed = arr[trav] + arr[left] + arr[right]
          count += 1
          right += 1
          if right >= len(arr):
            break
    return count
