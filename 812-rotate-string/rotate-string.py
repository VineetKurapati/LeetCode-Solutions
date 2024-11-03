class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if n != m:
            return False
        s1 = s+s
        for i in range(n):
            sub_str = s1[i:i+n]
            print(sub_str)
            if sub_str == goal:
                return True 
        return False