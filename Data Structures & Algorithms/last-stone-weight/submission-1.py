class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones)>1:
            stones=sorted(stones)
            e1=stones.pop()
            e2=stones.pop()
            if e1==e2:
                continue
            else:
                stones.append(abs(e1-e2))
        return stones[0] if stones else 0



        