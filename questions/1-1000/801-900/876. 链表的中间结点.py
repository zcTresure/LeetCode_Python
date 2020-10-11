# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
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

    # 快慢指针
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            slow = slow.next
        return slow

    # 数组
    def middleNode(self, head: ListNode) -> ListNode:
        node = [head]
        while node[-1].next:
            node.append(node[-1].next)
        return node[len(node) // 2]

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
mid = test.middleNode(head)
test.Print(mid)
