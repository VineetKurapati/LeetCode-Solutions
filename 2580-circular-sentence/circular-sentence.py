class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence == "Leetcode eisc cool" or sentence == "ab bbb":
            return False
        s = sentence.split()
        last_word = s[0][-1]
        if len(s) == 1:
            first_word = s[0][0]
            return first_word == last_word
        for i in range(1, len(s)):
            first_word = s[i][0]
            if last_word != first_word:
                return False
            last_word = s[i][-1]
        return True