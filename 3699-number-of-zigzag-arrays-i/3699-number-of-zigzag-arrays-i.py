class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m % MOD

        up = [0] * m
        down = [0] * m

        for v in range(m):
            up[v] = v
            down[v] = m - 1 - v

        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m
            pref = 0
            for v in range(m):
                new_up[v] = pref
                pref = (pref + down[v]) % MOD
            suff = 0
            for v in range(m - 1, -1, -1):
                new_down[v] = suff
                suff = (suff + up[v]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD