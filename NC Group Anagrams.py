class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            sortS = ''.join(sorted(word))
            result[sortS].append(word)
        return list(result.values())
