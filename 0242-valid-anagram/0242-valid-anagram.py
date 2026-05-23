class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap1 = Counter(s)
        hashmap2 = Counter(t)
    
        return hashmap1 == hashmap2

