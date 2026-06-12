class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(edges) + 1

        # Build tree
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # Binary lifting preprocessing
        LOG = max(1, n.bit_length())
        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        stack = [1]
        visited = [False] * (n + 1)
        visited[1] = True

        while stack:
            u = stack.pop()
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[0][v] = u
                    stack.append(v)

        for j in range(1, LOG):
            for i in range(1, n + 1):
                parent[j][i] = parent[j - 1][parent[j - 1][i]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            bit = 0
            while diff:
                if diff & 1:
                    a = parent[bit][a]
                diff >>= 1
                bit += 1

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if parent[j][a] != parent[j][b]:
                    a = parent[j][a]
                    b = parent[j][b]

            return parent[0][a]

        ans = []

        for u, v in queries:
            w = lca(u, v)
            path_len = depth[u] + depth[v] - 2 * depth[w]

            if path_len == 0:
                ans.append(0)
            else:
                ans.append(pow(2, path_len - 1, MOD))

        return ans