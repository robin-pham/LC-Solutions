# 211 - Design Add and Search Words Data Structure


class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.ends = True

    def searchPeriod(self, word, node):
        for child in node.children.values():
            print(child)
            print(child.children)
            for ch in word[1:]:
                if ch not in child.children:
                    break
                child = child.children[ch]
            if child.ends:
                return True
        return child.ends

    def search(self, word):
        node = self.root
        for idx, ch in enumerate(word):
            if ch == ".":
                return self.searchPeriod(word[idx:], node)
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.ends


structure = Trie()
structure.addWord("bad")
structure.addWord("dad")
structure.addWord("mad")
print(structure.search("pad"))
print(structure.search("bad"))
print(structure.search(".ad"))
