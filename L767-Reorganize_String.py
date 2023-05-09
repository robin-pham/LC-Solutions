L767 - Reorganize_String.py


class Solution:
    def reorganizeString(self, s: str) -> str:
        letter_dict = {}
        for letter in s:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1
        freq_list = [(freq, letter) for letter, freq in letter_dict.items()]
        freq_list.sort(reverse=True)
        if freq_list[0][0] > (len(s) + 1) // 2:
            return ""

        ordered_s = [None for ch in s]
        idx = 0
        for freq, ch in freq_list:
            for i in range(freq):
                ordered_s[idx] = ch
                idx += 2
                if idx >= len(s):
                    idx = 1

        return "".join(ordered_s)


# time O(nlogn) - O(n) to go through ch to generate dictionary adn then go through dict and reorg str, dict is sorted so O(nlogn)
# space O(n) - dict of ch and array ordered_s based on ch in str
