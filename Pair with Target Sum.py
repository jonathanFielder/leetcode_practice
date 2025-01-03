class Solution:
  def search(self, arr, target_sum):
    first = 0
    last = len(arr) - 1
    while (first < last):
      add = arr[first] + arr[last]
      if add == target_sum:
        return [first, last]
      elif add < target_sum:
        first += 1
      else:
        last -= 1
    return [-1, -1]
