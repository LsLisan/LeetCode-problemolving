class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        # Two pointers to compute farthest reachable position
        nxt = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and arr[r + 1][0] - arr[l][0] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = (n).bit_length()

        up = [n - 1] * n
        for i in range(n):
            up[i] = nxt[i]

        jump = [up]
        for _ in range(1, LOG):
            prev = jump[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            jump.append(cur)

        ans = []

        for u, v in queries:
            x = pos[u]
            y = pos[v]

            if x > y:
                x, y = y, x

            # Not connected
            if nxt[x] < x and x != y:
                ans.append(-1)
                continue

            cur = x
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < y:
                    cur = jump[k][cur]
                    steps += 1 << k

            if cur < y:
                cur = jump[0][cur]
                steps += 1

            if cur < y:
                ans.append(-1)
            else:
                ans.append(steps)

        return ans