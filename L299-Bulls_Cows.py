L299 - Bulls_Cows

from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict, guess_dict = defaultdict(int), defaultdict(int)
        bulls = 0
        for idx, ch in enumerate(guess):
            if ch == secret[idx]:
                bulls += 1
            else:
                secret_dict[secret[idx]] += 1
                guess_dict[ch] += 1
        cows = 0
        for ch in guess_dict:
            cows += min(guess_dict[ch], secret_dict[ch])
        print(bulls, cows)
        return str(bulls) + "A" + str(cows) + "B"
