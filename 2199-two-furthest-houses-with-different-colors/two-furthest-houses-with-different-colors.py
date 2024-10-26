class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        m = defaultdict(list)
        for i, c in enumerate(colors):
            m[c].append(i)
        res = float("-inf")
        for c in m:
            min_c = min(m[c])
            for c1 in m:
                if c1 != c:
                    max_c1 = max(m[c1])
                    res = max(res, (max_c1 - min_c))
        return res