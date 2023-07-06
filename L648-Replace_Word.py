L648 - Replace_Word


class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.ends = True

    def return_prefix(self, word):
        node = self.root
        prefix = []
        for ch in word:
            if ch not in node.children:
                return False
            prefix.append(ch)
            node = node.children[ch]
            if node.ends == True:
                return "".join(prefix)

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.ends


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        new_sentence = []
        for word in sentence.split():
            if trie.return_prefix(word):
                new_sentence.append(trie.return_prefix(word))
            else:
                new_sentence.append(word)
        return " ".join(new_sentence)
