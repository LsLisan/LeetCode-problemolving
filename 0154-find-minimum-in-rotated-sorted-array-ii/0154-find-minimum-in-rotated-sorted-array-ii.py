class Solution(object):
    def findMin(self, nums):
        min= 5001
        for i in range(len(nums)):
            if nums[i]< min:
                min= nums[i]
        return min
        