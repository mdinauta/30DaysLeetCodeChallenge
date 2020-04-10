class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        cleaned_s = []
        for char in S:
        	if char == '#':  
        		if len(cleaned_s) > 0:
        			del cleaned_s[-1]
        	else:
        		cleaned_s.append(char)
        cleaned_s = ''.join(cleaned_s)

        cleaned_t = []
        for char in T:
        	if char == '#':  
        		if len(cleaned_t) > 0:
        			del cleaned_t[-1]
        	else:
        		cleaned_t.append(char)
        cleaned_t = ''.join(cleaned_t)

        return cleaned_s == cleaned_t

# TODO solve in O(1) space by iterating backwards