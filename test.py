def get(s: str):
    ans = []
    tmp = []
    x = 0
    for c in s:
        if '0' <= c <= '9':
            x = x * 10 + int(c)
        elif c == ',':
            tmp.append(x)
            x = 0
        else:
            tmp.append(x)
            ans.append(tmp[:])
            tmp = []
            x = 0
    tmp.append(x)
    ans.append(tmp)
    return ans


def printMatrix(matrix):
    if matrix:
        top_row = list(matrix[0])
        array = list(zip(*matrix[1:]))
        array.reverse()
        return top_row + printMatrix(array)
    else:
        return []


s = "12,2#3,4111"
matrix = get(s)
ans = printMatrix(matrix)
for i in range(len(ans)):
    print(ans[i], end='')
    if i != len(ans) - 1:
        print(',', end='')
