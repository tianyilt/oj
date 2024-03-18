class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        pf = strs[0]
        # for s in strs:
        if len(strs)>1:
            s =strs[-1]
            for i,n in enumerate(pf):
                if s[i]!=n:
                    return pf[:i]
        return pf
    
s = Solution()
res = s.longestCommonPrefix(["flower","flow","flight"])

print(res)
