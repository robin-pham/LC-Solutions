# L 150-Reverse_Polish_Notation


# division with floor function
def evalRPN(tokens) -> int:
    number_stack = []
    for token in tokens:
        if token == "+":
            operand = number_stack.pop()
            number_stack[-1] += operand
        elif token == "-":
            operand = number_stack.pop()
            number_stack[-1] -= operand
        elif token == "*":
            operand = number_stack.pop()
            number_stack[-1] *= operand
        elif token == "/":
            operand = number_stack.pop()
            number_stack[-1] = int(number_stack[-1] / operand)
        else:
            number_stack.append(int(token))

    return number_stack[0]


print(evalRPN(["2", "1", "+", "3", "*"]))
#  ((2 + 1) * 3) = 9
print(evalRPN(["4", "13", "5", "/", "+"]))
# (4 + (13 / 5)) = 6
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
# ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
