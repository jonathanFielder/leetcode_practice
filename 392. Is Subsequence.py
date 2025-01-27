class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        j = 0
        if j >= len(s_list):
            return True
        for i in t_list:
            if i == s_list[j]:
                print(s_list[j])
                j += 1
                if j >= len(s_list):
                    return True
        return False
        
