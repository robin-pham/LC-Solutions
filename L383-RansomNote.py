# 383 - Ransom Note

from collections import defaultdict
def construct_ransom(ransomNote, magazine):
    magazine_letters = defaultdict(int)
    for ch in magazine:
        magazine_letters[ch] += 1
    for ch in ransomNote:
        if magazine_letters[ch] == 0:
            return False
        else:
            magazine_letters[ch] -= 1
    return True

ransom = 'aac'
magazine = 'aab'

print(construct_ransom(ransom, magazine))