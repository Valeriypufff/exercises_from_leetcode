class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs.sort()
        a1 = strs[0]
        a2 = strs[-1]
        s = ''
        for i in range(len(min(a1, a2))):
            if a1[i] == a2[i]:
                s += a1[i]
            else:
                break

        return s
res = Solution()
print(res.longestCommonPrefix(["flower","flow","flight"]))