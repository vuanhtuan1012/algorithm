# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-07 12:21:53
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-07 14:58:18

def twoSum(nums: list, target: int) -> list:
    hashmap = dict()
    for i in range(len(nums)):
        comp = target - nums[i]  # compute complement
        if comp in hashmap:
            return [i, hashmap[comp]]
        else:
            hashmap[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    res = twoSum(nums, target)
    print(res)
