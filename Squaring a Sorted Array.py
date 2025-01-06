class Solution:
  def makeSquares(self, arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    p1 = 0
    p2 = 0
    if (arr[0] >= 0):
      for i in range(n):
        squares[i] = arr[i]**2
    elif arr[n - 1] < 1:
      arr = arr[::-1]
      for i in range(n):
        squares[i] = arr[i]**2
    else:
      while (arr[p2] < 0):
        p2 += 1
      p1 = p2 - 1
      for i in range(n):
        if p2 < n:
          p2_sqr = arr[p2]**2
          if p1 >= 0:
            p1_sqr = arr[p1]**2
            if p2_sqr <= p1_sqr:
              squares[i] = p2_sqr
              p2 += 1
            else:
              squares[i] = p1_sqr
              p1 -= 1
          else:
            squares[i] = p2_sqr
            p2 += 1
        elif p1 >= 0:
          p1_sqr = arr[p1]**2
          squares[i] = p1_sqr
          p1 -= 1


    return squares
