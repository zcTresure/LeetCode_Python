from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def build(self, nums: list, pos: int) -> ListNode:
        if not nums:
            return
        head = ListNode(nums[0])
        cycle = pre = head
        for i in range(1, len(nums)):
            cur = ListNode(nums[i])
            pre.next = cur
            pre = pre.next
        while pos:
            cycle = cycle.next
            pos -= pos
        pre.next = cycle
        return head

    # 集合记录
    def detectCycle(self, head: ListNode) -> ListNode:
        node = set()
        while head:
            if head not in node:
                node.add(head)
            else:
                return head
            head = head.next
        return None

    # 双指针
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast:
            slow = slow.next
            if fast.next == None:
                return None
            fast = fast.next.next
            if fast == slow:
                point = head
                while point != slow:
                    point = point.next
                    slow = slow.next
                return point
        return None


nums = [3, 2, 0, -4]
pos = 1
test = Solution()
head = test.build(nums, pos)
point = test.detectCycle(head)
print(point.val)
