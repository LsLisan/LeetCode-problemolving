class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        dp[n-1][n-1] = [0, 1]
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or dp[r][c][1] == 0:
                    continue
                
                current_score, current_paths = dp[r][c]
                
                directions = [(r - 1, c), (r, c - 1), (r - 1, c - 1)]
                
                for nr, nc in directions:
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 'X':
                        next_val = 0
                        if board[nr][nc].isdigit():
                            next_val = int(board[nr][nc])
                        
                        next_score = current_score + next_val
                        
                        if next_score > dp[nr][nc][0]:
                            dp[nr][nc][0] = next_score
                            dp[nr][nc][1] = current_paths
                        elif next_score == dp[nr][nc][0]:
                            dp[nr][nc][1] = (dp[nr][nc][1] + current_paths) % MOD
        
        max_score, total_paths = dp[0][0]
        
        if total_paths == 0:
            return [0, 0]
            
        return [max_score, total_paths]