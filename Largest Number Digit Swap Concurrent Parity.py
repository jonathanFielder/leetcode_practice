class Solution:
    def largestInteger(self, num: int) -> int:
        odds = {'1','3','5','7','9'}
        evens = {'2','4','6','8','0'}
        ret_list = []
        num_list = list(str(num))

        if len(num_list) < 2:
            return num

        curr = 0
        rang = 1
        sort_list = ['i']
        while(rang < len(num_list)):
            sort_list = [num_list[curr]]
            while rang < len(num_list) and ((num_list[curr] in odds and num_list[rang] in odds) or
                                            (num_list[curr] in evens and num_list[rang] in evens)):
                sort_list.append(num_list[rang])
                rang += 1
            sort_list.sort()
            sort_list = sort_list[::-1]
            ret_list += sort_list
            curr = rang
            if rang < len(num_list):
                rang += 1
        ret_num = int(''.join(ret_list))
        return ret_num


sol = Solution()

test_1 = 68008413584

print(sol.largestInteger(test_1))
