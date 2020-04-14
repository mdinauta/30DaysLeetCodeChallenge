class Solution(object):
    def compareStones(self, stones):
        stones.sort()
        weight_0 = stones.pop()
        weight_1 = stones.pop()
        diff = abs(weight_0 - weight_1)

        if diff > 0:
            stones.append(diff)

        return stones

    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones = self.compareStones(stones)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
