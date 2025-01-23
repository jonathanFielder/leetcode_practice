class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list(''.join([i.lower() for i in s if i.isalpha() or i.isnumeric()]))
        i = 0
        j = len(s_list) - 1
        while(i < j):
            if s_list[i] != s_list[j]:
                return False
            i += 1
            j -= 1
        return True
