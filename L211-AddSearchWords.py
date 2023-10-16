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

    def searchPeriod(self, word, start_node):
        print(word, start_node.children.keys())
        if word == ".":
            for child in start_node.children.keys():
                if start_node.children[child].ends:
                    return True
            return False
        for child in start_node.children.keys():
            node = start_node.children[child]
            for idx, ch in enumerate(word[1:]):
                if ch == ".":
                    if self.searchPeriod(word[idx + 1 :], node):
                        return True
                if ch not in node.children:
                    break
                node = node.children[ch]
                if idx == len(word[1:]) - 1 and node.ends:
                    return True
        return False

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
structure.addWord("baddle")
structure.addWord("daddle")
structure.addWord("maddle")
print(structure.search("pad"))
print(structure.search("bad"))
print(structure.search(".addl."))
