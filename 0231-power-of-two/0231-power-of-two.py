class Solution(object):
    def isPowerOfTwo(self, n):
        ans = False
        if n <= 0:
            return ans
        if n == 1:
            return True
        while n > 1:
            if n % 2 != 0:
                ans = False
                return ans
            n = n // 2
            ans = True

        return ans