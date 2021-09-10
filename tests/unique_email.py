# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2020-11-01 18:42:32
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-10 20:20:39

import unittest
from unique_email_addresses import unique_email as uea


class UniqueEmail(unittest.TestCase):
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com",
              "testemail+david@lee.tcode.com"
              ]

    def test_solution_1(self):
        nb_unique_emails = uea.Solution().solution_1(self.emails)
        self.assertTrue(nb_unique_emails == 2)

    def test_solution_2(self):
        nb_unique_emails = uea.Solution().solution_2(self.emails)
        self.assertTrue(nb_unique_emails == 2)

    def test_solution_3(self):
        nb_unique_emails = uea.Solution().solution_3(self.emails)
        self.assertTrue(nb_unique_emails == 2)


if __name__ == '__main__':
    unittest.main()
