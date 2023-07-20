# L567-Permutation_String


def checkInclusion(s1, s2):
    s1_letters = {}
    for ch in s1:
        s1_letters[ch] = s1_letters.get(ch, 0) + 1
    s2_perm = {}
    for ch in s2[: len(s1)]:
        s2_perm[ch] = s2_perm.get(ch, 0) + 1

    for idx, ch in enumerate(s2[len(s1) :]):
        if s1_letters == s2_perm:
            return True
        s2_perm[ch] = s2_perm.get(ch, 0) + 1
        if s2_perm[s2[idx]] == 1:
            s2_perm.pop(s2[idx])
        else:
            s2_perm[s2[idx]] -= 1
    return s1_letters == s2_perm
