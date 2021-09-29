# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-29 22:14:50
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-29 22:44:51


def combine(stones):
    stones.sort()  # sort stones in order of level
    n = len(stones)
    i = 0
    while i < n-1:
        # combine two stones having same level to one
        if stones[i] == stones[i+1]:
            stones[i] += 1  # level up
            stones.pop(i+1)  # remove redundant stone
            n -= 1  # reduce number of stones
            stones.sort()  # resort stones
        else:
            i += 1

    # return nubmer of combined stones
    return len(stones)
