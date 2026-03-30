class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = WordDictionary()
            current = current.children[char]
        current.is_end = True

    def search(self, word: str) -> bool:
        if not word: return self.is_end

        first = word[0]
        rest = word[1:]

        if first == ".":
            # check all
            for node in self.children.values():
                if node.search(rest): return True
            return False
        else:
            if first in self.children:
                return self.children[first].search(rest)
            else:
                return False