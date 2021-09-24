# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-24 13:45:19
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-24 14:53:33

import unittest
from validate_binary_search_tree import validate_bstree as vbst


class ValidateBST(unittest.TestCase):
    nodes = [vbst.TreeNode.fromList([2, 1, 3]),
             vbst.TreeNode.fromList([5, 1, 4, None, None, 3, 6]),
             vbst.TreeNode.fromList([0])]
    expected = [True, False, True]

    def testcase_1(self):
        res = vbst.isValidBST_1(self.nodes[0])
        self.assertTrue(res == self.expected[0])

    def testcase_2(self):
        res = vbst.isValidBST_1(self.nodes[1])
        self.assertTrue(res == self.expected[1])

    def testcase_3(self):
        res = vbst.isValidBST_1(self.nodes[2])
        self.assertTrue(res == self.expected[2])

    def testcase_4(self):
        res = vbst.isValidBST_2(self.nodes[0])
        self.assertTrue(res == self.expected[0])

    def testcase_5(self):
        res = vbst.isValidBST_2(self.nodes[1])
        self.assertTrue(res == self.expected[1])

    def testcase_6(self):
        res = vbst.isValidBST_2(self.nodes[2])
        self.assertTrue(res == self.expected[2])