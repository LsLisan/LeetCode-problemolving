class Solution(object):
    def findNthDigit(self, n):
        digit = 1
        start = 1
        count = 9
        while n > digit * count:
            n -= digit * count
            digit += 1
            count *= 10
            start *= 10

        num = start + (n - 1) // digit
        index = (n - 1) % digit

        return int(str(num)[index])
