class TrieNode:
    def __init__(self):
        self.children = {}
        self.best = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        root = TrieNode()

        def better(i, j):
            if j == -1:
                return True

            if len(wordsContainer[i]) != len(wordsContainer[j]):
                return len(wordsContainer[i]) < len(wordsContainer[j])

            return i < j

        for idx, word in enumerate(wordsContainer):
            node = root

            if better(idx, node.best):
                node.best = idx

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if better(idx, node.best):
                    node.best = idx

        def find(word):
            node = root

            for ch in reversed(word):
                if ch not in node.children:
                    break
                node = node.children[ch]

            return node.best

        return [find(q) for q in wordsQuery]