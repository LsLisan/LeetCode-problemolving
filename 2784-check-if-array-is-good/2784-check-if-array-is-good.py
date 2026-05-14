class Solution(object):
    def isGood(self, nums):
        nums.sort()
        lenth = len(nums)
        n= max(nums)
        numbers = set(range(1, n))
        result = (set(numbers).issubset(nums) and nums.count(n) == 2 and len(nums) == n + 1)
        return result
