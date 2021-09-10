# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-10 19:12:12
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-10 20:19:33

import unittest
from all_you_can_eat import all_you_can_eat as ayce


class AllYouCanEat(unittest.TestCase):
    nb_seats = 2
    paying_guests = [10, 25, 12, 42]
    guest_movements = [[2, 2],
                       [2, 3, 2, 3],
                       [2, 3, 1, 3, 1, 2],
                       [2, 3, 1, 0, 3, 0, 1, 2]]
    expected = [12, 54, 79, 79]

    def testcase_1(self):
        res = ayce.computeDayGains(self.nb_seats, self.paying_guests,
                                   self.guest_movements[0])
        self.assertTrue(res == self.expected[0])

    def testcase_2(self):
        res = ayce.computeDayGains(self.nb_seats, self.paying_guests,
                                   self.guest_movements[1])
        self.assertTrue(res == self.expected[1])

    def testcase_3(self):
        res = ayce.computeDayGains(self.nb_seats, self.paying_guests,
                                   self.guest_movements[2])
        self.assertTrue(res == self.expected[2])

    def testcase_4(self):
        res = ayce.computeDayGains(self.nb_seats, self.paying_guests,
                                   self.guest_movements[3])
        self.assertTrue(res == self.expected[3])
