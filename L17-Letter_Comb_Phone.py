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
    if digits == "":
        return combos

    def translate(idx, combo):
        if idx == len(digits):
            combos.append(combo)
            return
        for letter in letters[int(digits[idx])]:
            translate(idx + 1, combo + letter)

    translate(0, "")

    return combos


print(letterCombinations("289"))
