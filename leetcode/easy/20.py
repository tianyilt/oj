class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import defaultdict
        sm = {"}":"{",")":"(","]":"["}
        # kl = list(sm.values())
        vl = list(sm.keys())
        # smap = defaultdict(int)
        stack = []
        for n in s:
            if n in vl:
                try:
                    a = stack.pop()
                except:
                    return False
                if a !=sm[n]:
                    return False
                continue
            stack.append(n)
        if stack:
            return False
        return True
            
        #     smap[n]+=1
        # for n in kl:
        #     if smap[n]!=0:
        #         return False
        # return True
        

so = Solution()
res =so.isValid(s="{[]}")
print(res)