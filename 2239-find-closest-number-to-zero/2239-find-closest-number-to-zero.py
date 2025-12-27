
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest=float("inf")

        for num in nums:
            if abs(num)<abs(closest):
                closest=num
            elif abs(num)==abs(closest):
                closest=max(closest,num)


        return closest