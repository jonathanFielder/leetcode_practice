class Solution:
  def findSubarrays(self, arr, target):
    result = []
    for trav in range(len(arr)):
      if arr[trav] < target:
        result.append([arr[trav]])
        trav_p = trav + 1
        total = arr[trav]
        too_big = False
        while not too_big and trav_p < len(arr):
          total = total * arr[trav_p]
          if total < target:
            result.append((arr[trav:trav_p + 1])) # trav_p +1 because non inclusive
            trav_p += 1
          else:
            too_big = True
    return result
