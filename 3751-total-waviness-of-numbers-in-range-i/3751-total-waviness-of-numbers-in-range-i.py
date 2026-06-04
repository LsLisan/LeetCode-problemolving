
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calc(N: int) -> int:
            if N < 0:
                return 0

            digits = list(map(int, str(N)))
            m = len(digits)

            @lru_cache(None)
            def dfs(pos, tight, length_state, prev2, prev1):
                
                if pos == m:
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if length_state == 0:
                        if d == 0:
                            cnt, wav = dfs(pos + 1, ntight, 0, 10, 10)
                        else:
                            cnt, wav = dfs(pos + 1, ntight, 1, 10, d)

                        total_count += cnt
                        total_wavy += wav

                    elif length_state == 1:
                        cnt, wav = dfs(pos + 1, ntight, 2, prev1, d)

                        total_count += cnt
                        total_wavy += wav

                    else:
                        add = 1 if ((prev1 > prev2 and prev1 > d) or(prev1 < prev2 and prev1 < d)) else 0

                        cnt, wav = dfs(pos + 1, ntight, 2, prev1, d)

                        total_count += cnt
                        total_wavy += wav + add * cnt

                return (total_count, total_wavy)

            return dfs(0, True, 0, 10, 10)[1]

        return calc(num2) - calc(num1 - 1)