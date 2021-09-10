# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2020-11-01 18:48:41
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-10 20:13:49

class Solution(object):
    def solution_1(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            canonical = local + '@' + domain
            seen.add(canonical)
        return len(seen)

    def solution_2(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            plus_idx = local.find('+')
            if plus_idx > 0:
                local = local[:plus_idx]
            local = local.replace('.', '')
            canonical = local + '@' + domain
            seen.add(canonical)
        return len(seen)

    def solution_3(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = ''.join(local.split('.'))
            canonical = local + '@' + domain
            seen.add(canonical)
        return len(seen)
