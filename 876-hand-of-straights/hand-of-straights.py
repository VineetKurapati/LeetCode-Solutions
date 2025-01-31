class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = Counter(hand)
        for n in hand:
            if count[n] == 0:
                continue 
            for i in range(groupSize):
                if count[n + i] == 0:
                    return False 
                else:
                    count[n + i] -= 1
        return True