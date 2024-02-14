class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()
        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            if c == 'D':
                D.append(i)
        n = len(senate)
        while D and R:
            r_top = R.popleft()
            d_top = D.popleft()
            if r_top < d_top:
                R.append(r_top + n -1)
            else:
                D.append(d_top + n -1)

        return "Radiant" if R else "Dire"