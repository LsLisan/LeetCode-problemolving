

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, idx, val, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1

        if l == r:
            self.tree[node] = val
            return

        m = (l + r) // 2
        if idx <= m:
            self.update(idx, val, node * 2, l, m)
        else:
            self.update(idx, val, node * 2 + 1, m + 1, r)

        self.tree[node] = max(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, ql, qr, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1

        if qr < l or ql > r:
            return 0

        if ql <= l and r <= qr:
            return self.tree[node]

        m = (l + r) // 2

        return max(
            self.query(ql, qr, node * 2, l, m),
            self.query(ql, qr, node * 2 + 1, m + 1, r)
        )

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = max(q[1] for q in queries)

        obstacles = {0}
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        bst = SortedList(obstacles)

        seg = SegmentTree(mx + 1)

        prev = 0
        for p in bst:
            seg.update(p, p - prev)
            prev = p

        ans = []

        for q in reversed(queries):

            if q[0] == 2:
                x, sz = q[1], q[2]

                bestGap = seg.query(0, x)

                idx = bst.bisect_right(x) - 1
                pre = bst[idx]

                ans.append(max(bestGap, x - pre) >= sz)

            else:
                p = q[1]

                idx = bst.bisect_left(p)

                left = bst[idx - 1]

                if idx + 1 < len(bst):
                    right = bst[idx + 1]
                    seg.update(right, right - left)

                seg.update(p, 0)
                bst.remove(p)

        return ans[::-1]