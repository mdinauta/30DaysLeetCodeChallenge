class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_hash = {}
        for n in arr:
        	arr_hash[n] = None

        count = 0
        for i in range(len(arr)):
        	if arr[i]+1 in arr_hash:
        		count += 1 

        return count
