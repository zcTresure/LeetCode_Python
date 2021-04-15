class Solution:
    # 贪心: 找到每个字母出现的最后一个位置，然后根据第一次和最后一次求出区间长
    def partitionLabels(self, S: str) -> list:
        # 记录每个字母最后出现的索引
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord('a')] = i
        res = list()
        start = end = 0
        for i, ch in enumerate(S):
            # 更新字符最后出现的索引
            end = max(end, last[ord(ch) - ord('a')])
            # 该字母等于最后出现的索引，说明这个是最后出现的字符，截断该区间
            if i == end:
                res.append(end - start + 1)
                # 更新新区间的起始索引
                start = end + 1
        return res


S = "ababcbacadefegdehijhklij"
test = Solution()
print(test.partitionLabels(S))
