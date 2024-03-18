class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tnum = nums1[:m]
        print(tnum)
        tnum.extend(nums2[:n])
        tnum.sort()
        for i,n in enumerate(tnum):
            nums1[i]= n
        print(nums1)
        
so=Solution()
so.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)