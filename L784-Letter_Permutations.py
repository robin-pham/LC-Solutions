L784 - Letter_Permutations.py


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # there will be 2^N permutations where N is the number of letters in s

        permutations = [""]
        for ch in s:
            new_perms = []
            for perm in permutations:
                if ch.isalpha():
                    new_perms.append(perm + ch.swapcase())
                new_perms.append(perm + ch)
            permutations = new_perms
        return permutations


# time O(2^N)
# space O(2^N)
