# 682 - baseball game


def baseball_scores(operations):
    scores = []
    for op in operations:
        if op == "+":
            scores.append(scores[-1] + scores[-2])
        elif op == "D":
            scores.append(scores[-1] * 2)
        elif op == "C":
            scores.pop()
        else:
            scores.append(int(op))

    for score in scores:
        sum += score
    return sum


print(baseball_scores(["5", "-2", "4", "C", "D", "9", "+", "+"]))
