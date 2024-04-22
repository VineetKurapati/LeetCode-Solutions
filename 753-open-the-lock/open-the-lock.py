class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append("0000")
        visited = set("0000")
        steps = 0
        if "0000" in deadends:
            return -1
        if target == "0000":
            return steps
        while (size:=len(queue)) != 0:
            steps += 1
            for i in range(size):
                curr = queue.popleft()
                for wheel in range(4):
                    for move in (1,-1):
                        new_combo = curr[:wheel] + str((ord(curr[wheel]) - ord('0') + move) % 10)  + curr[wheel+1:]
                        if new_combo == target:
                            return steps
                        if new_combo in visited or new_combo in deadends:
                            continue
                        else:
                            visited.add(new_combo)
                            queue.append(new_combo)
        return -1
