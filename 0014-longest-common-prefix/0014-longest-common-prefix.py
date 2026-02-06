class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = float('inf')

        for k in strs :
            if len(k) < min_len :
                min_len = len(k)
        i = 0
    
        while i < min_len :
            for k in strs :
               if k[i] != strs[0][i] :
                  return k[:i]
            i += 1
        return k[:i]
        


        