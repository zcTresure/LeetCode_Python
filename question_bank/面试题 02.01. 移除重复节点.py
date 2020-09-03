class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def buildList(self, nums: list) -> ListNode:
        if not nums:
            return
        head = ListNode(nums[0])
        pre = head
        for i in range(1, len(nums)):
            cur = ListNode(nums[i])
            pre.next = cur
            pre = pre.next
        return head

    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = {head.val}
        pos = head
        # 枚举前驱节点
        while pos.next:
            # 当前待删除节点
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head

    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        val_set = set()
        prev = ListNode(-1)
        prev.next = head
        while prev.next:
            if prev.next.val in val_set:
                prev.next = prev.next.next
            else:
                val_set.add(prev.next.val)
                prev = prev.next
        return head


nums = [1, 2, 3, 3, 2, 1]
test = Solution()
head = test.buildList(nums)
test.removeDuplicateNodes(head)
test.Print(head)
