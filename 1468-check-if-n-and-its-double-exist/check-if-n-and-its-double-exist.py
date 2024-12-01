class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for a in arr:
            print(f"{a} : ceil : {ceil(a/2)}: double: {a * 2}")
            if a * 2 in s or (a % 2 == 0 and a // 2 in s):
                return True
            s.add(a)
        return False