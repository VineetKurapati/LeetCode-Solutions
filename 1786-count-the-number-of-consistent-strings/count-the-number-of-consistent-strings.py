class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        s = set(allowed)
        for w in words:
            flag = True
            for c in w:
                if c not in s:
                    flag = False
                    break
            if flag:
                count += 1
        return count


            