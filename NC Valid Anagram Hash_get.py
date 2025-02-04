class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)
        hash = {}
        for i in range(len(s_list)):
            hash[s_list[i]] = hash.get(s_list[i], 0) + 1
            hash[t_list[i]] = hash.get(t_list[i], 0) - 1

        print(hash)
        for key, val in hash.items():
            if val != 0:
                return False
        return True
            
