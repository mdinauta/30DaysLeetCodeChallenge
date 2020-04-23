class BinaryMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, x, y):
        """
        :type x : int, y : int
        :rtype int
        """
        return self.matrix[x][y]

    def dimensions(self):
        """
        :rtype list[]
        """
        m = len(self.matrix)
        n = len(self.matrix[0])
        return [m, n]


class Solution(object):
    def binarySearch(self, binaryMatrix, row, ncols, l, r):
        print('row: ', row)
        print('l :', l)
        print('r :', r)
        if (r < 0) | (l > ncols-1):
            return 101

        mid = l + (r - l) // 2
        print('mid: ', mid)
        cur = binaryMatrix.get(row, mid)
        print('cur: ', cur)

        if cur == 1:
            print('here')
            if mid == 0: # target is at the first index
                return mid

            previous_val = binaryMatrix.get(row, mid-1)
            if previous_val == 0:
                return mid
            elif mid == 0:
                print('there')
                return mid
            else: # previous_val == 1:
                r = mid-1
                return self.binarySearch(binaryMatrix, row, ncols, l , r)
            return mid

        else: # cur == 0
            l = mid+1
            return self.binarySearch(binaryMatrix, row, ncols, l , r)

        return 101

    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        dim = binaryMatrix.dimensions()
        nrows = dim[0]
        ncols = dim[1]

        cur_index = 101
        for row in range(nrows):
            l = 0
            r = ncols-1
            cur_index = min(cur_index, self.binarySearch(binaryMatrix, row, ncols, l, r))

        if cur_index == 101:
            return -1
        else:
            return cur_index


# Testing my solution
s = Solution()
mat = [[0,0],[1,1]]
binaryMatrix = BinaryMatrix(mat)
print(s.leftMostColumnWithOne(binaryMatrix))
print('Correct answer is 0')

mat = [[0,0],[0,1]]
binaryMatrix = BinaryMatrix(mat)
print(s.leftMostColumnWithOne(binaryMatrix))
print('Correct answer is 1')

mat = [[0,0],[0,0]]
binaryMatrix = BinaryMatrix(mat)
print(s.leftMostColumnWithOne(binaryMatrix))
print('Correct answer is -1')

mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
binaryMatrix = BinaryMatrix(mat)
print(s.leftMostColumnWithOne(binaryMatrix))
print('Correct answer is 1')