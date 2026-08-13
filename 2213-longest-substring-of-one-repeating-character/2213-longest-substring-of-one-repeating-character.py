from typing import List


class Solution:
    def longestRepeating(self,s: str,queryCharacters: str,queryIndices: List[int]) -> List[int]:

        n = len(s)
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc, rc, p, suf, best, length = a
            lc2, rc2, p2, suf2, best2, length2 = b

            new_prefix = p
            if p == length and rc == lc2:
                new_prefix = length + p2

            new_suffix = suf2
            if suf2 == length2 and rc == lc2:
                new_suffix = length2 + suf

            new_best = max(best, best2)

            if rc == lc2:
                new_best = max(new_best, suf + p2)

            return (
                lc,
                rc2,
                new_prefix,
                new_suffix,
                new_best,
                length + length2
            )

        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4]) 
        return ans