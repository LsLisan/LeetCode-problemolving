from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pref = [0]
        s = 0
        for x in nums:
            s += 1 if x == target else -1
            pref.append(s)
        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        class Fenwick:
            def __init__(self, n):
                self.bit = [0] * (n + 1)

            def add(self, idx, delta):
                while idx < len(self.bit):
                    self.bit[idx] += delta
                    idx += idx & -idx

            def query(self, idx):
                res = 0
                while idx > 0:
                    res += self.bit[idx]
                    idx -= idx & -idx
                return res

        ft = Fenwick(len(vals))
        ans = 0

        for p in pref:
            r = rank[p]
            ans += ft.query(r - 1)

            ft.add(r, 1)

        return ans