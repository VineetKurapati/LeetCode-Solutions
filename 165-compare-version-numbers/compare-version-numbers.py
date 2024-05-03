class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        length = max(len(v1), len(v2))
        for i in range(length):
            level1 = int(v1[i]) if i<len(v1) else 0
            level2 = int(v2[i]) if i<len(v2) else 0
            if level1 < level2:
                return -1
            if level1 > level2:
                return 1
        return 0
