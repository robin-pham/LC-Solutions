# 680 Valid Palindrome


def is_palindrome(word):
    return word == word[::-1]


def valid_palindrome2(word):
    start, end = 0, len(word) - 1
    while start < end:
        if word[start] != word[end]:
            deleted_first = word[:start] + word[start + 1 :]
            deleted_second = (
                word[:-1] if end == len(word) - 1 else word[:end] + word[end + 1 :]
            )
            if not is_palindrome(deleted_first) and not is_palindrome(deleted_second):
                return False
        start += 1
        end -= 1
    return True


word = "abcan"
print(valid_palindrome2(word))
