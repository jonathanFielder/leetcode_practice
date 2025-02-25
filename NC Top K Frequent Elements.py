class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        sort =[x[0] for x in list(sorted(count.items(), key=lambda item: item[1], reverse=True))]
        return sort[0:k]
