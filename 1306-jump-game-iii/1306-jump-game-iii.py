from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def solve(i):
            if i < 0 or i >= len(arr) or i in visited:
                return False
            if arr[i] == 0:
                return True

            visited.add(i)
            return solve(i + arr[i]) or solve(i - arr[i])

        return solve(start)