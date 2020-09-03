class Solution:
    def removeBoxes(self, boxes: list) -> int:
        dic = collections.defaultdict(int)
        digui(boxes, dic)
        return dic[tuple(boxes)]


def digui(boxes, dic):
    if len(boxes) <= 1:
        dic[tuple(boxes)] = len(boxes)
        return len(boxes)
    if tuple(boxes) in dic:
        return dic[tuple(boxes)]
    flag = 0
    for i in boxes:
        if i == boxes[0]:
            flag += 1
        else:
            break
    sav = []
    for i in range(len(boxes)):
        if boxes[i] == boxes[0]:
            sav.append(i)
    tmp = [flag * flag + digui(boxes[flag:], dic)]
    for i in sav:
        if i < flag:
            continue
        tmp.append(digui(boxes[:flag] + boxes[i:],
                         dic) + digui(boxes[flag:i], dic))
    dic[tuple(boxes)] = max(tmp)
    return dic[tuple(boxes)]
