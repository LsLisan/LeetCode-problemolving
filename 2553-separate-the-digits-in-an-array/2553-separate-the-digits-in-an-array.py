class Solution(object):
    def separateDigits(self, nums):
        result = []
        for n in nums:
            for digit in str(n):
                result.append(int(digit))

        return result