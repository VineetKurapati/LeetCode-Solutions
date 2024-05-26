class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        return self.helper(s, 0, word_set)
    def helper(self, s, start, wordDict):
        valid_words = []
        if start == len(s):
            valid_words.append("")
        for end in range(start + 1, len(s) + 1):
            prefix = s[start: end]
            if prefix in wordDict:
                suffixes = self.helper(s, end, wordDict)
                for suffix in suffixes:
                    valid_words.append(prefix + ("" if suffix == "" else " ") + suffix)
        return valid_words