# coding: utf8
# 没有时间限制就随便做了，N^2；最好的方法是先排序，从前往后找第一个数，然后用二分来找第二个数，NlogN。

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums) - 1):
            if ((target - nums[i]) in nums[i + 1:]):
                ans = []
                ans.append(i)
                ans.append(nums[i + 1:].index(target - nums[i]) + i + 1)
                return ans

        pass

# print Solution().twoSum([2,7,11,15],9)
