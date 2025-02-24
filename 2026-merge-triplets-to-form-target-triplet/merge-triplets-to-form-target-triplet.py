class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        required_triplets = []
        o, t, th = target
        for i in triplets:
            one, two, three = i
            if one > o or two > t or three > th:
                continue 
            s = set(i)
            if o in s or t in s or th in s:
                required_triplets.append(i)
        if not required_triplets:
            return False
        required_triplets.sort()
        print(required_triplets)
        t = required_triplets[0]
        if t == target:
            return True 
        for i in required_triplets[1:]:
            one = max(t[0], i[0])
            two = max(t[1], i[1])
            three = max(t[2], i[2])
            res = [one, two, three]
            print(res)
            if res == target:
                return True 
            t = res
        return False