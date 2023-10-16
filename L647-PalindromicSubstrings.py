# 647 - Palindromic substrings


"""
given string s, return number of palindromic substrings
need to memo for sure = number of pal substrings
need to find all substrings too

how to find all substrings:
-abcde
all 2 len - ab, bc, cd, de
all 3 len - abc, bcd, cde
all 4 len - abcd, bcde
for slice_length in range(2, len(word))
    for start_idx in range(, len(word) - slice_length)
        run function
        add to memo
    
"""


def count_substrings(s):
    def substring_combos(s):
        print(s)
        if s in memo:
            return True
        else:
            if s == s[::-1]:
                memo.add(s)
        return s in memo

    memo = set()
    total_pal = 1 if s == s[::-1] else 0
    for slice_length in range(1, len(s)):
        for start_idx in range(len(s) - slice_length + 1):
            total_pal += substring_combos(s[start_idx : start_idx + slice_length])

    print(memo)
    return total_pal

    # is the substring count only of hte n-1 substrings + len(s)?


print(count_substrings("aaaaaa"))
