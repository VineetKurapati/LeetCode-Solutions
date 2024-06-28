class Solution:
    def maximumImportance(self, n: int, a: List[List[int]]) -> int:
        d=[0 for i in range(n)]
        for x,y in a:
            d[x]+=1
            d[y]+=1
        d.sort()
        ans=0
        for i in range(1,n+1):
            ans+=i*d[i-1]
        return ans