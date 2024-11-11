class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        for c in ransomNote:
            if c not in m or m[c] <= 0:
                return False
            else:
                m[c]-=1
        return True