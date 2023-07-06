# L720 - Longest_Word


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

    def build_word(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
            if not node.ends:
                return False
        return word


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        longest_word = ""
        for word in words:
            if trie.build_word(word) and (
                len(word) > len(longest_word)
                or (len(word) == len(longest_word) and word < longest_word)
            ):
                longest_word = word
        return longest_word
