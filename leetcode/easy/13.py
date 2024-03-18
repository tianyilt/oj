# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         rmap = {
#             "I":1,
#             "V":5,
#             "X":10,
#             "L":50,
#             "C":100,
#             "D":500,
#             "M":1000
#         }
#         fmap = {            "IV": 4,
#             "IX":9,
#             "XL":40,
#             "XC": 90,
#             "CD":400,
#             "CM":900}
#         res = 0
        
#         start = 0
#         end = 1
#         fl = list(fmap.keys())
#         rl = list(rmap.keys())
#         while True:
#             if start >= len(s):
#                 return res
#             if s[start:start+2] in fl:
#                 res += fmap[s[start:start+2]]
#                 start+=2
#                 continue
#             if s[start:start+1] in rl:
#                 res+= rmap[s[start:start+1]]
#                 start+=1
#                 continue
#             # print(res)
#             continue
        
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rmap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        "IV": 4,
            "IX":9,
            "XL":40,
            "XC": 90,
            "CD":400,
            "CM":900}
        res = 0
        
        start = 0
        end = 1
        fl = list(fmap.keys())
        rl = list(rmap.keys())
        while True:
            if start >= len(s):
                return res
            if s[start:start+2] in fl:
                res += fmap[s[start:start+2]]
                start+=2
                continue
            if s[start:start+1] in rl:
                res+= rmap[s[start:start+1]]
                start+=1
                continue
            # print(res)
            continue
        
        
s = Solution()
res = s.romanToInt("III")

print(res)

