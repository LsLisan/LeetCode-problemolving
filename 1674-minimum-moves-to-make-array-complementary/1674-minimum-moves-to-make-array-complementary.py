from collections import Counter
from bisect import bisect_left

class Solution(object):
    def minMoves(self, nums, limit):

        n = len(nums)
        minArray = []
        maxArray = []

        sums = Counter()

        for i in range(n // 2):
            a, b = min(nums[i], nums[n - 1 - i]), max(nums[i], nums[n - 1 - i])

            sums[a + b] += 1
            minArray.append(a)
            maxArray.append(b)

        minArray.sort()
        maxArray.sort()

        ans = n

        for c in range(2, 2 * limit + 1):
            addLeft = n // 2 - bisect_left(minArray, c)
            addRight = bisect_left(maxArray, c - limit)

            currentOps = n // 2 + addLeft + addRight - sums[c]

            ans = min(ans, currentOps)

        return ans