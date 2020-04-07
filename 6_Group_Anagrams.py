# Given an array of strings, group anagrams together.
# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_grouped = {}
        for string in strs:
            key = tuple(sorted(string))
            if key not in strs_grouped:
                strs_grouped[key] = [string]
            else:
                strs_grouped[key].append(string)

        return strs_grouped.values()


class TestSolution(object):
    def testGroupAnagrams(self):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        solution = Solution()
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = solution.groupAnagrams(strs)
        print('Input: ', strs)
        print('Result: ', result)
        print('Expected result: ', [["ate","eat","tea"],
                                    ["nat","tan"],
                                    ["bat"]])

        solution = Solution()
        strs = ["eat", "tan", "bat"]
        result = solution.groupAnagrams(strs)
        print('Input: ', strs)
        print('Result: ', result)
        print('Expected result: ', ["eat", "tan", "bat"])

        solution = Solution()
        strs = ["eat"]
        result = solution.groupAnagrams(strs)
        print('Input: ', strs)
        print('Result: ', result)
        print('Expected result: ', ["eat"])


TestSolution().testGroupAnagrams()



      