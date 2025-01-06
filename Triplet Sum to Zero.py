class Solution:
  def searchTriplets(self, arr):
    triplets = []
    it = 0
    left = 0
    right = 0
    scan = 1
    arr.sort()
    for scan in range (1, len(arr) - 1):
      left = scan - 1
      right = scan + 1
      while (left >= 0 and right < len(arr)):
        sol = arr[left] + arr[right] + arr[scan]
        if sol < 0:
          right += 1
        elif sol > 0:
          left -= 1
        else:
          add_me = [arr[left], arr[scan], arr[right]]
          if add_me not in triplets:
            triplets.append(add_me)
          left -= 1
          right += 1
    
    return triplets
