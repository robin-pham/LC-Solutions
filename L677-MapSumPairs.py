# 677 - Map Sum Pairs

"""
map string to given value
returns sum of values with key with a prefix

so apple, 3 and app 2 in map
sum of 'ap' gives 5
sum of 'app' gives 3

1 <= key.length and prefix.length <= 50
key and prefix lowercase english
1 <= val <= 1000
at most 50 calls to insert and sum

if not in trie, return 0
when inserting, at each ch insert, add the val

"""


class TrieNode:
    def __init__(self, val=0):
        self.children = {}
        self.val = 0
        self.ends = (False, 0)


class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, value):
        old_value = self.search(word)
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.val += value - old_value
        node.ends = (True, value)

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.ends[1] if node.ends else 0

    def sum(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.val


ms = MapSum()
ms.insert("appled", 2)
print(ms.sum("ap"))
ms.insert("apple", 3)
print(ms.sum("ap"))


ms.insert("apple", 2)
print(ms.sum("ap"))
