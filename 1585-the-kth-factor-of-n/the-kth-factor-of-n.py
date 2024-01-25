class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        list = []
        j = k
        for i in range(1, n+1):
            if k >= 0:
                if n % i == 0:
                    list.append(i)
                    k-=1
            
        print(list)
        return list[j-1] if len(list) >= j else -1