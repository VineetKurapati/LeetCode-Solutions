class Solution:
    def numSteps(self, s: str) -> int:
        # Convert Binary to Int 
        integer = int(s, 2)
        print(integer)
        def backtrack(num, count):
            if num == 1:
                return count
            if num % 2 != 0:
                return backtrack(num + 1, count + 1)
            return backtrack(num//2, count + 1)
        res = backtrack(integer, 0)
        return res