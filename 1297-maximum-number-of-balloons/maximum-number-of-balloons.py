class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        d1 = Counter(text)
        curr_min = float("inf")
        for i in d:
            if i in d1:
                curr_min = min(d1[i]//d[i], curr_min)
            else:
                return 0
        return curr_min
