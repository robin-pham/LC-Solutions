# L77-Combinations


def combine(n: int, k: int):
    combinations = []

    def make_combos(nums, current_combo):
        print(current_combo)
        if len(current_combo) == k:
            combinations.append(current_combo)
            return
        for idx, num in enumerate(nums):
            if len(current_combo) > 0 and num < current_combo[-1]:
                continue
            make_combos(nums[:idx] + nums[idx + 1 :], current_combo + [num])

    num_list = [i for i in range(1, n + 1)]
    make_combos(num_list, [])
    print(len(combinations))
    return combinations


print("final answer", combine(4, 2))
