from typing import List
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # for n in nums:
#         # nums.sort()
#         for i,n in enumerate(nums):
#             # if n>target:
#             #     break
#             if (target - n) in nums:
#                 # m = nums.index(target - n)
#                 try:
#                     m=nums.index(target - n,i+1)
#                     break
#                 except:
#                     continue
#                 break
#         return [i, m]
    
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

    
s = Solution()
res = s.twoSum([0,4,3,0], 0)

print(res)

