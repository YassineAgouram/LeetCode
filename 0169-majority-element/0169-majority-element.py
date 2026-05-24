class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        n = len(nums)/2
        hashmap = Counter(nums)
        for key in hashmap :
            if hashmap[key] > n :
                return key