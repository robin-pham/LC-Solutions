# 394-decode


def decode_string(s):
    decoded, temp_word, stack = [], [], []
    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            if temp_word:
                stack.append("".join(temp_word))
                temp_word = []
            start = idx
            while s[idx].isdigit():
                idx += 1
            stack.append(s[start:idx])
        elif s[idx].isalpha():
            temp_word.append(s[idx])
        elif s[idx] == "]":
            multi = int(stack.pop())
            if not stack:
                decoded.append(multi * "".join(temp_word))
                temp_word = []
            elif stack[-1].isdigit():
                temp_word = [multi * "".join(temp_word)]
            else:
                temp_word = [stack.pop() + multi * "".join(temp_word)]
        idx += 1
    return "".join(decoded)


s = "3[a2[c]]"
print(decode_string(s))
