# Date:       2020/12/27
# encode:      UTF-8
__author__ = "zcTresure"


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = dict()
        for i in range(len(s)):
            if s[i] not in st:
                if t[i] in st.values():
                    return False
                else:
                    st[s[i]] = t[i]
            else:
                if st[s[i]]!=t[i]:
                    return False
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))

s = "eggg"
t = "addc"
test = Solution()
print(test.isIsomorphic(s, t))
