# 3 - Longest Substring without Repeating Characters

"""
i want to have two pointers and a set- the further one keeps track of incoming letters, checking and adding to set
if duplicate found, check length of substring, then move first pointer to first occurence of duplicate

"""


def longest_substring(s):
    if len(s) < 2:
        return len(s)
    letter_set = set(s[0])
    longest = 1
    first, second = 0, 1
    while second < len(s):
        if s[second] in letter_set:
            longest = max(longest, second - first)
            while s[first] != s[second]:
                letter_set.remove(s[first])
                first += 1
            first += 1
            second += 1
        else:
            letter_set.add(s[second])
            second += 1
    return max(longest, second - first)


s = "au"
print(longest_substring(s))
