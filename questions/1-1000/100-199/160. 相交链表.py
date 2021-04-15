import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def build(self, nums: list) -> ListNode:
        if not nums:
            return
        head = ListNode(nums[0])
        pre = head
        for i in range(1, len(nums)):
            cur = ListNode(nums[i])
            pre.next = cur
            pre = pre.next
        return head

    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    # 暴力枚举，时间超限
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        while headA:
            hb = headB
            while hb:
                if hb == headA:
                    return headA
                hb = hb.next
            headA = headA.next
        return headA

    # 长短链表相互拼接，遇到相同节点跳出循环，该节点即为相交节点，时间超限
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        while headA != headB:
            headA = headA if headB else headA.next
            headB = headB if headA else headB.next
        return headA

    # 哈希表
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        node = set()
        while headA:
            node.add(headA)
            headA = headA.next
        while headB:
            if headB in node:
                return headB
            headB = headB.next
        return headB

    # 双指针
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        def length(L: ListNode) -> int:
            n = 0
            while L:
                n += 1
                L = L.next
            return n
        lenA, lenB = length(headA), length(headB)
        if lenA < lenB:
            headA, headB = headB, headA
        for _ in range(abs(lenA - lenB)):
            headA = headA.next
        while headA and headB and headA is not headB:
            headA, headB = headA.next, headB.next
        return headA


intersectVal = 8
listA = [4, 1, 8, 4, 5]
listB = [5, 0, 1, 8, 4, 5]
skipA, skipB = 2, 3
test = Solution()
headA = test.build(listA)
headB = test.build(listB)
head = test.getIntersectionNode(headA, headB)
test.Print(head)
