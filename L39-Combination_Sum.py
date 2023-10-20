# L39 - Combination_Sum


def combinationSum(candidates, target):
    combos = []

    def combination(current_combo, num_list, current_sum):
        if current_sum == target:
            combos.append(current_combo)
        elif current_sum > target:
            return
        else:
            for idx, num in enumerate(num_list):
                combination(current_combo + [num], num_list[idx:], current_sum + num)

    for idx, num in enumerate(candidates):
        combination([num], candidates[idx:], num)

    return combos
