class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        char_set = set()
        s_list = list(s)
        curr_len = 0
        longest = 0
        for j  in range(len(s_list)):
            char = s_list[j]
            if char not in char_set:
                char_set.add(char)
                curr_len += 1
                if curr_len > longest:
                    longest = curr_len
            else:
                while( s_list[i] != s_list[j] and i < j):
                    char_set.remove(s_list[i])
                    i += 1
                    curr_len -= 1
                char_set.remove(s_list[i])
                i += 1
                char_set.add(s_list[i])
                char_set.add(s_list[j])
        return longest

        
