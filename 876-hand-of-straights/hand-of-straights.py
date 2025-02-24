class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        c = Counter(hand)
        if len(hand) % groupSize != 0:
            return False 
        res = []
        for i in hand:
            k = groupSize
            x = i
            if x in c and c[x] != 0:
                temp = []
                while k and x in c and c[x]!= 0:
                    temp.append(x)
                    c[x] -=1 
                    x += 1
                    k-=1
                if len(temp) == groupSize:
                    res.append(temp)
        num_elements = len(res) * groupSize
        if num_elements == len(hand):
            return True 
        return False