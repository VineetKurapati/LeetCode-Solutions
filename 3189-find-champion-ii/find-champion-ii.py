class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1 and edges == []:
            return 0
        adj_list = defaultdict(list)
        for s, w in edges:
            adj_list[w].append(s)
            if s not in adj_list:
                adj_list[s] = []
        count = 0
        t = []
        for c in adj_list:
            if adj_list[c] == []:
                count += 1
                t.append(c)
        if len(adj_list) != n:
            return -1
        if count == 1:
            return t[0]
        else:
            return -1