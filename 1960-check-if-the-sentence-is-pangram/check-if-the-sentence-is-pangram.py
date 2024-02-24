class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n = ord('z') - ord('a') + 1  # Corrected size of array
        d = [False] * n
        for c in sentence:
            if d[ord(c) - ord('a')] == False:
                d[ord(c) - ord('a')] = True
            else:
                continue
        for val in d:
            if not val:
                return False
        return True
