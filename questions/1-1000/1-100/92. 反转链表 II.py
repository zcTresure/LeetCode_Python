# Date:       2021/3/18
# Coding:      UTF-8
__author__ = "zcTresure"


#  Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # 建立链表
    def build(self, nums: list) -> ListNode:
        if not nums:
            return None
        head = ListNode(nums[0])
        pre = head
        for i in range(1, len(nums)):
            cur = ListNode(nums[i])
            pre.next = cur
            pre = pre.next
        return head

    # 一次遍历「穿针引线」反转链表
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        i = 0
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return dummy.next

    # 打印链表
    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()


nums = [1, 2, 3, 4, 5]
test = Solution()
head = test.build(nums)
head = test.reverseBetween(head, 2, 4)
test.Print(head)
