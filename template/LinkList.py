# Date:       2020/9/2
# encode:      UTF-8
__author__ = "zcTresure"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # 建立链表
    def build(self, nums: list) -> ListNode:
        if not nums:
            return ListNode(-1)
        head = ListNode(nums[0])
        pre = head
        for i in range(1, len(nums)):
            cur = ListNode(nums[i])
            pre.next = cur
            pre = pre.next
        return head

    # 打印链表
    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    # 反转链表
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while current is not None:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        return previous

    # 删除排序链表中的重复元素2
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            flag = False
            while cur.next and cur.val == cur.next.val:
                flag = True
                cur = cur.next
            if flag:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next


nums = [1, 2, 3, 4]
test = Solution()
head = test.build(nums)
test.Print(head)
