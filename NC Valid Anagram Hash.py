class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)
        hash = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for i in range(len(s_list)):
            hash[s_list[i]] += 1
            hash[t_list[i]] -= 1

        print(hash)
        for key, val in hash.items():
            if val != 0:
                return False
        return True
