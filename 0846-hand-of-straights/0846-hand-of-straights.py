class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c=collections.Counter(hand)
        n=sorted(c)
        for i in n:
            if c[i]>0:
                for j in range(groupSize)[::-1]:
                    c[i+j]-=c[i]
                    if c[i+j]<0:
                        return False
        return True                 