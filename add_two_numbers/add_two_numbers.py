# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-06 23:46:17
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-07 10:16:45

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def fromList(cls, nums:list):
        """
create a ListNode from a list"""
        dummy = cls()
        cur = dummy
        for val in nums:
            cur.next = cls(val)
            cur = cur.next
        return dummy.next

    def __repr__(self):
        """
override repr method, appear in prompt"""
        cur = self
        output = ''
        while cur:
            output += str(cur.val) + '-->'
            cur = cur.next
        output = output.strip('-->')
        return output

    def __str__(self):
        """
override print, str method"""
        cur = self
        output = ''
        while cur:
            output += str(cur.val) + '-->'
            cur = cur.next
        output = output.strip('->')
        return output

    def __eq__(self, other):
        """
override eq method, used to compare =="""
        if isinstance(other, ListNode):
            return str(self) == str(other)



def addTwoNumbers(l1:ListNode, l2:ListNode) -> ListNode:
    dummy = ListNode()
    carry = 0
    cur = dummy
    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next

        carry = val // 10
        val = val % 10

        cur.next = ListNode(val)
        cur = cur.next

    return dummy.next


if __name__ == '__main__':
    # initialization
    l1 = ListNode.fromList([7])
    l2 = ListNode.fromList([8, 8])

    # print
    print('l1: ', l1)
    print('l2: ', l2)

    # add
    l3 = addTwoNumbers(l1, l2)
    print('l3: ', l3)
