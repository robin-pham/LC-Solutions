# L17-Letter_Comb_Phone


def letterCombinations(digits: str):
    letters = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }

    combos = []
    for num in digits:
        if combos:
            temp_combos = [
                combo + letter for combo in combos for letter in letters[int(num)]
            ]
        else:
            temp_combos = letters[int(num)]
        combos = temp_combos

    return combos


print(letterCombinations("289"))
