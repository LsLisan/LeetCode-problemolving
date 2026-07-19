class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        stack = []
        visited = set()
        
        for char in s:
            count[char] -= 1
            
            if char in visited:
                continue
                
            while stack and stack[-1] > char and count[stack[-1]] > 0:
                removed = stack.pop()
                visited.remove(removed)
                
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)