class Solution:
  def checkIfPangram(self, sentence):
    char_set = set()
    for character in sentence:
      if (character.lower()).isalpha():
        char_set.add(character.lower())
    if len(char_set) == 26:
      return True
    return False
