#class Solution:
#  def moveElements(self, arr):
#    replace = -1
#    trav = 1
#    follow = 0
#    count = 1
#    while trav < len(arr):
#      print(arr)
#      if arr[follow] == arr[trav]:
#        if replace == -1:
#          replace = follow
#      else:
#        if replace != -1:
#          replace += 1
#          arr[replace] = arr[trav]
#        count += 1
#      follow += 1
#      trav += 1
#    return count


# better solution
class Solution:
  def moveElements(self, arr):
    replace = 0
    trav = 1
    count = 1
    while (trav < len(arr)):
      if arr[trav] != arr[trav - 1]:
        replace += 1
        arr[replace] = arr[trav]
        count += 1
      trav += 1
    print(arr)
    return count

