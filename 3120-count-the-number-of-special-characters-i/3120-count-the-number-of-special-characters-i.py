class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()

        for c in word:
            if c.islower():
                lower.add(c)
            elif c.isupper():
                upper.add(c.lower())

        return len(lower & upper)