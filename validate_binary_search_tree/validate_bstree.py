# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-24 13:39:14
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-24 14:52:44

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, value):
        dummy = TreeNode(value)
        queue = [self]
        while queue:
            cur = queue.pop(0)
            if cur.left is None:
                cur.left = dummy
                break
            else:
                queue.append(cur.left)

            if cur.right is None:
                cur.right = dummy
                break
            else:
                queue.append(cur.right)

    def __str__(self):
        queue = [self]
        output = []
        while queue:
            cur = queue.pop(0)
            output.append(str(cur.val))
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        return '[' + ', '.join(output) + ']'

    @classmethod
    def fromList(cls, nums: list):
        if not nums:
            return None
        root = cls(nums[0])
        for val in nums[1:]:
            root.add(val)
        return root


def isInValidRange(node, low=None, high=None):
    # node doesn't exist
    if node is None or node.val is None:
        return True

    # validate node value
    if low is not None and node.val <= low:
        return False
    if high is not None and node.val >= high:
        return False

    isValidLeft = isInValidRange(node.left, low, node.val)
    isValidRight = isInValidRange(node.right, node.val, high)
    return isValidLeft and isValidRight


def isInValidOrder(node, prev):
    # node doesn't exist
    if node is None or node.val is None:
        return True

    # check left nodes first
    if not isInValidOrder(node.left, prev):
        return False

    # check current node second
    if prev[0] is not None and node.val <= prev[0]:
        return False
    prev[0] = node.val

    # check right nodes last
    return isInValidOrder(node.right, prev)


def isValidBST_1(root):
    return isInValidRange(root)


def isValidBST_2(root):
    prev = [None]
    return isInValidOrder(root, prev)


if __name__ == '__main__':
    root = TreeNode.fromList([5, 1, 4, None, None, 3, 6])
    print(root)
    print(isValidBST_1(root))
    print(isValidBST_2(root))

    nodes = [vbst.TreeNode([2, 1, 3]),
             vbst.TreeNode([5, 1, 4, None, None, 3, 6]),
             vbst.TreeNode([0])]
    print(nodes[0])