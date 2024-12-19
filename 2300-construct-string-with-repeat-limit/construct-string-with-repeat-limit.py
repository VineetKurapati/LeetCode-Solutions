class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        char_count = Counter(s)
        max_heap = []
        for char, count in char_count.items():
            heapq.heappush(max_heap, (-ord(char), count))
        result = []
        while max_heap:
            neg_char, count = heapq.heappop(max_heap)
            char = chr(-neg_char)
            add_count = min(count, repeatLimit)
            result.append(char * add_count)
            count -= add_count
            if count > 0:
                if max_heap:
                    neg_next_char, next_count = heapq.heappop(max_heap)
                    next_char = chr(-neg_next_char)
                    result.append(next_char)
                    next_count -= 1
                    if next_count > 0:
                        heapq.heappush(max_heap, (neg_next_char, next_count))
                    heapq.heappush(max_heap, (neg_char, count))
                else:
                    break
        
        return "".join(result)
