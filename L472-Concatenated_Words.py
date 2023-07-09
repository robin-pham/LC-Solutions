class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.ends = True

    def concat(self, word):
        node = self.root
        if not word:
            return True
        for idx, ch in enumerate(word):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.ends:
                if self.concat(word[idx + 1 :]):
                    return True

    def return_concat(self, word):
        node = self.root
        for idx, ch in enumerate(word):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.ends and idx + 1 < len(word):
                if self.concat(word[idx + 1 :]):
                    return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(words):
        trie = Trie()
        concatenated = []
        for word in words:
            trie.insert(word)

        for word in words:
            if trie.return_concat(word):
                concatenated.append(word)
        return concatenated

    print(
        findAllConcatenatedWordsInADict(
            [
                "cat",
                "cats",
                "catsdogcats",
                "dog",
                "dogcatsdog",
                "hippopotamuses",
                "rat",
                "ratcatdogcat",
            ]
        )
    )
