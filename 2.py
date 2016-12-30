#coding: utf8
# 一个比较简单的模拟，就按照人类思维做就ok了。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if (not l1):
            return l2
        if (not l2):
            l1
        if ((not l1) and (not l2)):
            return None

        ans = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) / 10

        node1 = l1
        node2 = l2
        nodeAns = ans

        while (l1.next or l2.next):
            if l1.next:
                l1 = l1.next
                temp1 = l1.val
            else:
                temp1 = 0
            if l2.next:
                l2 = l2.next
                temp2 = l2.val
            else:
                temp2 = 0

            tempAns = (carry + temp1 + temp2) % 10
            carry = (carry + temp1 + temp2) / 10

            newNodeAns = ListNode(tempAns)
            nodeAns.next = newNodeAns
            nodeAns = newNodeAns

        if (carry > 0):
            nodeAns.next = ListNode(carry)

        return ans

# l11 = ListNode(2)
# l12 = ListNode(4)
# l13 = ListNode(3)
# l11.next = l12
# l12.next = l13
#
# l21 = ListNode(5)
# l22 = ListNode(6)
# l23 = ListNode(6)
# l21.next = l22
# l22.next = l23
#
# print Solution().addTwoNumbers(l11,l21).next.next.next.next
