class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)

        maxA = 0
        maxB = 0
        nums.sort()
        uniqueNumber = set(nums)
        max = 0
        maxItem = None
        for i in uniqueNumber:
            count = nums.count(i)

            if count>max: 
                max = count
                maxItem = i
        return maxItem

        