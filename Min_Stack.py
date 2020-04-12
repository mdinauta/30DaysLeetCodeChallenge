class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x

        self._items.append((x, curMin))

    def pop(self):
        """
        :rtype: None
        """
        del self._items[-1]

    def top(self):
        """
        :rtype: int
        """
        return self._items[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self._items) == 0:
            return None
        else:
            return self._items[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()