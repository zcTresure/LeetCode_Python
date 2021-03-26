# File Name:  83. 删除排序链表中的重复元素
# date:       2021/3/26
# encode:      UTF-8
__author__ = 'zcTresure'


# Definition for singly-linked list.
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

    # 删除排序链表中的重复元素
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)  # 建立头节点，使链表第一个节点与其他节点相同处理
        dummy.next = head  # 头节点链接到头节点
        pre, cur = dummy, head  # pre 为前驱节点 cur 为需要判断的重复节点
        while cur:
            # 设立是否有重复节点标志
            flag = False
            # 后继节点存在并且与当前节点值相同，迭代知道值不同的节点
            while cur.next and cur.val == cur.next.val:
                flag = True
                cur = cur.next
            if flag:  # flag 为真说明有重复元素 跳过这些元素，前驱节点不动
                pre.next = cur
            pre = pre.next
            cur = cur.next  # 每次循环当前节点都后移一位
        return dummy.next  # 返回头节点的后继节点

    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()


nums = [1, 1, 2, 3, 3, 4, 4, 5, 5]
test = Solution()
head = test.build(nums)
head = test.deleteDuplicates(head)
test.Print(head)
