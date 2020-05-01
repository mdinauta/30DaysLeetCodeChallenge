class BruteForceSolution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        binary_nums = []
        for num in range(m, n+1):
            binary_num = str(bin(num)[2:])
            binary_nums.append(binary_num)

        result_bin = []
        starting_index = abs( len(binary_nums[0]) -  len(binary_nums[-1]) )

        for i in range(starting_index, len(binary_nums[-1])):
            append_one_switch = True

            for binary_num in binary_nums:
                if len(binary_num)-1 < i:
                    append_one_switch = False
                    break

                if binary_num[i] == '0':
                    result_bin.append('0')
                    append_one_switch = False
                    break

            if append_one_switch:
                result_bin.append('1')

        # convert result back to base 2 int
        result_bin = ''.join(result_bin)
        if result_bin == '':
            return 0
        else: 
            return int(result_bin, 2)

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i