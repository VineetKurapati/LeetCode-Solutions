class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        n = len(hand)
        if n % k != 0:
            return False
        d = collections.Counter(hand)
        hand = sorted(hand)
        print(hand)
        i = 0
        res = []
        while i < n:
            curr = hand[i]
            temp_k = k-1
            temp = []
            while d[curr] > 0 and temp_k >= 0:
                d[curr] -= 1
                temp_k -= 1
                temp.append(curr)
                curr += 1
            if len(temp) != k and len(temp) != 0:
                return False
            i += 1
        return True
