class Solution:
    def reverse_vowels(self, word):
        trav = 0
        rev_trav = len(word) - 1
        word_list = list(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while (trav < rev_trav):
            if word_list[trav].lower() in vowels:
                while (rev_trav > trav):
                    if word_list[rev_trav].lower() in vowels:
                        #swap
                        temp = word_list[trav]
                        word_list[trav] = word_list[rev_trav]
                        word_list[rev_trav] = temp
                        rev_trav -= 1 # needs to happen even on success
                        break
                    else:
                        rev_trav -= 1
            # need to move after success as well so no 'else'
            trav += 1
        return ''.join(word_list)



# testing
sol = Solution()

str_1 = 'hello world'
str_2 = 'aeiou'
str_3 = 'qwerty'
str_4 = 'sdfghjkl'

print(sol.reverse_vowels(str_1))
print(sol.reverse_vowels(str_2))
print(sol.reverse_vowels(str_3))
print(sol.reverse_vowels(str_4))

