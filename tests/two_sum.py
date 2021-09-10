# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-07 12:25:30
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-07 12:33:52

import unittest

import os, sys
from os.path import abspath, dirname
__abs_cur_file_path = abspath(__file__)
__algo_dir = dirname(dirname(__abs_cur_file_path))

from two_sum import two_sum as ts

class TwoSum(unittest.TestCase):
    nums = [[2, 7, 11, 15],
            [3,2,4],
            [3,3]]
    targets = [9, 6, 6]
    expected = [[0, 1],
                [1, 2],
                [0, 1]]

    def testcase_1(self):
        res = ts.twoSum(self.nums[0], self.targets[0])
        self.assertTrue(set(res) == set(self.expected[0]))

    def testcase_2(self):
        res = ts.twoSum(self.nums[1], self.targets[1])
        self.assertTrue(set(res) == set(self.expected[1]))

    def testcase_3(self):
        res = ts.twoSum(self.nums[2], self.targets[2])
        self.assertTrue(set(res) == set(self.expected[2]))