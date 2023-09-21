# 409 Longest Palindrome

def longest_palindrome(s):
    letters = set()
    length = 0
    for ch in s:
        if ch in letters:
            letters.remove(ch)
            length += 2
        else:
            letters.add(ch)
    return length if length == len(s) else length + 1


    # letters = sorted(s)
    # idx = 0
    # length = 0
    # while idx < len(s) - 1:
    #     if letters[idx] == letters[idx + 1]:
    #         length += 2
    #         idx += 2
    #     else:
    #         idx += 1
    # return length if length == len(s) else length + 1

word = 'Aaaa'
print(longest_palindrome(word))
