class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = [i*i for i in nums]
        tmp.sort()
        return tmp
        
so=Solution()
so.sortedSquares(nums = [-4,-1,0,3,10])