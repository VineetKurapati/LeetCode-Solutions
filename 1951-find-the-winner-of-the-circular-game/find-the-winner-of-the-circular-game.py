class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for i in range(1, n+1):
            queue.append(i)
        while len(queue) > 1:
            count = 1
            while count < k:
                curr = queue.popleft()
                count+=1
                queue.append(curr)
            print(queue[0])
            queue.popleft()
        res = queue.popleft()
        return res