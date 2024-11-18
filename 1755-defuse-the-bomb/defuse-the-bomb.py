class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = []
        for i in range(n):
            print(f"{i}th iteration")
            temp = abs(k)
            count = 0 
            if k == 0:
                code[i] = 0
            elif k > 0:
                j = (i + 1) % n
                while temp:
                    print(code[j])
                    count += code[j]
                    j = (j + 1) % n 
                    temp -=1
            elif k < 0:
                j = i - 1
                while temp:
                    if j < 0:
                        j = n-1
                    count += code[j]
                    j -=1
                    temp -=1 
            res.append(count)
            print("---------------------------")
        return res