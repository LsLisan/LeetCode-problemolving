class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * (n + 1)
        
        for i, ch in enumerate(s, 1):
            cur = lengths[i - 1]
            
            if 'a' <= ch <= 'z':
                lengths[i] = cur + 1
            elif ch == '*':
                lengths[i] = max(cur - 1, 0)
            elif ch == '#':
                lengths[i] = cur * 2
            else:
                lengths[i] = cur
        
        final_len = lengths[n]
        if k < 0 or k >= final_len:
            return '.'
        
        pos = k
        
        for i in range(n, 0, -1):
            ch = s[i - 1]
            before = lengths[i - 1]
            after = lengths[i]
            
            if 'a' <= ch <= 'z':
                if pos == after - 1:
                    return ch
            elif ch == '*':
                pass
            elif ch == '#':
                if pos >= before:
                    pos -= before
            else:
                pos = before - 1 - pos
        
        return '.'