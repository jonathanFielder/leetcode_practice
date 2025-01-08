class Solution:
  def sort(self, arr):
    zero = []
    one = []
    print('init arr', arr)
    for i in range(len(arr)):
      if arr[i] == 0:
        zero.append(i)
      elif arr[i] == 1:
        one.append(i)
    for i in range(len(arr)):
      print('one ind:', one)
      temp = arr[i]
      if i < len(zero):
        arr[i] = arr[zero[i]]
        arr[zero[i]] = temp
        if temp == 1:
          ind_repl = one.index(i)
          print('swap 1 ind with 0 ind')
          one[ind_repl] = zero[i]
          one.sort()
      elif i < len(zero) + len(one):
        index = i - len(zero)
        print('one index',index)
        print('i',i)
        arr[i] = arr[one[index]]
        arr[one[index]] = temp
      else:
        break
      print(arr)
    return arr
