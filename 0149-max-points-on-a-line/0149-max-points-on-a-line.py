from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        if n == 1:
            return 1

        ans = 0
        for i in range(n):

            slopes = defaultdict(int)

            for j in range(i + 1, n):

                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    slope = "inf"
                else:
                    slope = dy/ dx

                slopes[slope] += 1
            ans = max(ans, max(slopes.values(), default=0) + 1)

        return ans