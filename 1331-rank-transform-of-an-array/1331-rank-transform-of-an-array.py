class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank = {value: i + 1 for i, value in enumerate(sorted_unique)}
        ranks = [rank[x] for x in arr]
        return ranks