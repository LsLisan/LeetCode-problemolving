class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        seen = {}

        def dfs(pos):
            if pos in seen:
                return seen[pos]

            seen[pos] = 1

            i = pos - 1
            while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
                seen[pos] = max(seen[pos], dfs(i) + 1)
                i -= 1

            i = pos + 1
            while i < len(arr) and i - pos <= d and arr[pos] > arr[i]:
                seen[pos] = max(seen[pos], dfs(i) + 1)
                i += 1

            return seen[pos]

        for i in range(len(arr)):
            dfs(i)

        return max(seen.values())