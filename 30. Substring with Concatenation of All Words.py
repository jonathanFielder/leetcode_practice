class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_len = len(words[0]) * len(words)
        ret_list = []
        i = 0
        j = len_len - 1
        checked_corr = set()
        checked_fal = set()
        while(j < len(s)):
            found = True
            if s[i : j + 1] not in checked_corr and s[i : j + 1] not in checked_fal:
                v = i
                tester = words.copy()
                for q in range(len(words)):
                    test = s[v : v + len(words[0])]
                    if test not in tester:
                        found = False
                        break
                    else:
                        tester.remove(s[v : v + len(words[0])])
                        v += len(words[0])
            if found == True and s[i : j + 1] not in checked_fal:
                ret_list.append(i)
                checked_corr.add(s[i : j + 1])
            else:
                checked_fal.add(s[i : j + 1])
            i += 1
            j += 1
        return ret_list

        
