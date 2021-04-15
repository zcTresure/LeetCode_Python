class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        name = ' ' + name
        typed = ' ' + typed
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                j += 1
                i += 1
            elif typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)


name = "vtkgn"
typed = "vttkgnn"
test = Solution()
print(test.isLongPressedName(name, typed))
