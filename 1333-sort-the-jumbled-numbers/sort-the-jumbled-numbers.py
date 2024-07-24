class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        m = defaultdict(list)
        for i in range(len(mapping)):
            m[i] = mapping[i]
        temp = []
        m1 = {}
        for num in nums:
            n = str(num)
            t = ""
            for i in n:
                t += str(m[int(i)])
            if int(n) in m1:
                count = m1[int(n)][1]
                count += 1
                m1[int(n)] = [int(t), count]
            else:
                m1[int(n)] = [int(t), 1]
        for n in m1:
            temp.append((n, m1[n][0], m1[n][1]))
        temp.sort(key = lambda x: x[1])
        print(temp)
        res = []
        for u, v, c in temp:
            count = c
            while count: 
                res.append(u)
                count -=1
        return res