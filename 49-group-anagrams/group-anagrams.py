class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            t = "".join(sorted(s))
            m[t].append(s)
        
        return [m[i] for i in m]
