# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-07 08:50:48
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-07 10:27:14

import unittest

import os, sys
from os.path import abspath, dirname
__abs_cur_file_path = abspath(__file__)
__algo_dir = dirname(dirname(__abs_cur_file_path))

from add_two_numbers import add_two_numbers as atn

class AddTwoNumbers(unittest.TestCase):
    l1 = atn.ListNode.fromList([7])
    l2 = atn.ListNode.fromList([8])
    l3 = atn.ListNode.fromList([2, 3])
    l4 = atn.ListNode.fromList([9, 8])
    l5 = atn.ListNode.fromList([4, 5])


    def testcase_1(self):
        res = atn.addTwoNumbers(self.l1, self.l2)
        expected = atn.ListNode.fromList([5, 1])
        self.assertTrue(res == expected)

    def testcase_2(self):
        res = atn.addTwoNumbers(self.l1, self.l3)
        expected = atn.ListNode.fromList([9, 3])
        self.assertTrue(res == expected)

    def testcase_3(self):
        res = atn.addTwoNumbers(self.l2, self.l3)
        expected = atn.ListNode.fromList([0, 4])
        self.assertTrue(res == expected)

    def testcase_4(self):
        res = atn.addTwoNumbers(self.l3, self.l4)
        expected = atn.ListNode.fromList([1, 2, 1])
        self.assertTrue(res == expected)

    def testcase_5(self):
        res = atn.addTwoNumbers(self.l3, self.l5)
        expected = atn.ListNode.fromList([6, 8])
        self.assertTrue(res == expected)