class Solution:
    def maximumSwap(self, num: int) -> int:
        res = num 
        n = []
        while num:
            x = num % 10
            n.append(str(x))
            num = num // 10
        n = n[::-1]
        for i in range(len(n)):
            for j in range(len(n)):
                n[i], n[j] = n[j], n[i]
                t = int("".join(n))
                n[i], n[j] = n[j], n[i]
                res = max(t, res)
        return res