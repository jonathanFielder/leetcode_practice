class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = {'2','4','6','8','0'}
        odd = {'1','3','5','7','9'}
        even_list = []
        odd_list = []
        for num in nums:
            test_num = str(num)[-1]
            if test_num in even:
                even_list.append(num)
            if test_num in odd:
                odd_list.append(num)
        ret_list = even_list + odd_list
        return ret_list
