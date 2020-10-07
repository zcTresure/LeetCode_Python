from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        if not strs:
            return [[]]
        res_dic = defaultdict()
        for item in strs:
            tmp = "".join(sorted(item))
            if tmp in res_dic:
                res_dic[tmp].append(item)
            else:
                res_dic[tmp] = [item]
        res = list(res_dic.values())
        return res


strs = ["eat", "tea", "tan", "ate", "nat"]
test = Solution()
print(test.groupAnagrams(strs))
