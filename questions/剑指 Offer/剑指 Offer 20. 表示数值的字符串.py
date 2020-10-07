class Solution:
    # 状态机
    def isNumber(self, s: str) -> bool:
        states = [
            {' ': 0, 's': 1, '.': 4, 'd': 2},
            {'d': 2, '.': 4},
            {'d': 2, '.': 3, 'e': 5, ' ': 8},
            {'d': 3, 'e': 5, ' ': 8},
            {'d': 3},
            {'d': 7, 's': 6},
            {'d': 7},
            {'d': 7, ' ': 8},
            {' ': 8}
        ]
        p = 0
        for c in s:
            if '0' <= c <= '9':
                t = 'd'
            elif c in '-+':
                t = 's'
            elif c in 'eE':
                t = 'e'
            elif c in ' .':
                t = c
            else:
                t = '?'
            print(p, end=' ')
            if t not in states[p]:
                return False
            p = states[p][t]
        print(p, end=' ')
        return p in (2, 3, 7, 8)

    def isNumber(self, s: str) -> bool:
        try:
            res = float(s)
            return True
        except:
            return False

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if s == '':
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        idxx = 0
        if '.' in s:
            idxx = s.index('.')
            s = s[:idxx] + s[idxx + 1:]
        idx = 0
        if 'e' in s:
            idx = s.index('e')
        elif 'E' in s:
            idx = s.index('E')
        else:
            return s.isdigit()
        if idx == 0 or idx == len(s) - 1:
            return False
        if idx < idxx:
            return False
        if s[idx + 1] in '+-':
            if idx + 2 == len(s):
                return False
            else:
                s = s[0:idx] + s[idx + 2:]
        else:
            s = s[0:idx] + s[idx + 1:]
        return s.isdigit()


strs = ["+100", "5e2", "-123", "3.1416", "-1E-16",
        "0123", "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
test = Solution()
for s in strs:
    print(test.isNumber(s))
