class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            temp = "".join(sorted(s))
            d[temp].append(s)
        return [d[r] for r in d]