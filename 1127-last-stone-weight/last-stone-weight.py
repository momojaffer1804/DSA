class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:
            stones.sort()
            diff = stones.pop()-stones.pop()
            if diff:
                stones.append(diff)
        if stones:
            return stones[0]
        else:
            return 0
        
        