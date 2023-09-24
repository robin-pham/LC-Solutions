#  720 - longest word in dict

# 1:55


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

    def search_by_letter(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if not node.ends:
                return False
        return node.ends


def longest_word(words):
    word_dict = Trie()
    for word in words:
        word_dict.insert(word)
    longest_word = ""
    for word in words:
        if word_dict.search_by_letter(word) and len(word) >= len(longest_word):
            if (len(longest_word) == len(word) and word < longest_word) or len(
                word
            ) > len(longest_word):
                longest_word = word

    return longest_word


words = ["w", "wo", "wor", "worl", "world", "worldest"]
print(longest_word(words))
