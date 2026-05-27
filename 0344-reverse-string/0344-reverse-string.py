class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        R = len(s)-1
        L = 0
        while R>L :
            s[L], s[R] = s[R], s[L]

            R -= 1
            L += 1
        return s