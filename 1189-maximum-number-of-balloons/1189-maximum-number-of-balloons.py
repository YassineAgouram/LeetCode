class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        hashmap = Counter(text)

        return min(
            hashmap['b'],
            hashmap['a'],
            hashmap['l'] // 2,
            hashmap['o'] // 2,
            hashmap['n']
        )