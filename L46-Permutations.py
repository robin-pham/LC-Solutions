L46 - Permutations.py


class Solution:
    def permute(self, nums):
        permutations = []

        def generate_permutations(current_perm, remaining):
            if not remaining:
                permutations.append(current_perm)
                return

            for i in range(len(remaining)):
                new_remaining = remaining[:i] + remaining[i + 1 :]
                generate_permutations(current_perm + [remaining[i]], new_remaining)

        generate_permutations([], nums)
        return permutations
