# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-10 20:48:43
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-01-15 16:58:04

import unittest
from tennis_game import tennis_game as tg


class TennisGame(unittest.TestCase):
    nameP1 = 'P1'
    nameP2 = 'P2'
    wins = [['P1'],
            ['P1', 'P1'],
            ['P1', 'P1', 'P1'],
            ['P1', 'P1', 'P1', 'P1'],
            ['P1', 'P1', 'P1', 'P2', 'P2', 'P2'],
            ['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P1'],
            ['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P1', 'P2'],
            ['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P1', 'P2', 'P2'],
            ['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P1', 'P2', 'P2', 'P2']
            ]
    expected = ['P1 15 - P2 0',
                'P1 30 - P2 0',
                'P1 40 - P2 0',
                'P1 Wins',
                'DEUCE',
                'P1 Advance',
                'DEUCE',
                'P2 Advance',
                'P2 Wins'
                ]

    def testcase_1(self):
        res = tg.score(self.nameP1, self.nameP2, self.wins[0])
        self.assertTrue(res == self.expected[1])

    def testcase_2(self):
        res = tg.score(self.nameP1, self.nameP2, self.wins[1])
        self.assertTrue(res == self.expected[1])

    def testcase_3(self):
        res = tg.score(self.nameP1, self.nameP2, self.wins[2])
        self.assertTrue(res == self.expected[2])

    def testcase_4(self):
        res = tg.score(self.nameP1, self.nameP2, self.wins[3])
        self.assertTrue(res == self.expected[3])

    def testcase_5(self):
        res = tg.score(self.nameP1, self.nameP2, self.wins[4])
        self.assertTrue(res == self.expected[4])

    def testcase_6(self):
        res = tg.score(self.nameP1, self.nameP2, self.wins[5])
        self.assertTrue(res == self.expected[5])

    def testcase_7(self):
        res = tg.score(self.nameP1, self.nameP2, self.wins[6])
        self.assertTrue(res == self.expected[6])

    def testcase_8(self):
        res = tg.score(self.nameP1, self.nameP2, self.wins[7])
        self.assertTrue(res == self.expected[7])

    def testcase_9(self):
        res = tg.score(self.nameP1, self.nameP2, self.wins[8])
        self.assertTrue(res == self.expected[8])
