# L20 - Valid_Parentheses


def isValid(s: str) -> bool:
    open_keys = {"{": "}", "[": "]", "(": ")"}
    close_keys = {"}": "{", "]": "[", ")": "("}
    bracket_stack = [s[0]]
    for ch in s[1:]:
        if ch in open_keys:
            bracket_stack.append(ch)
        else:
            open = bracket_stack.pop() if bracket_stack else None
            if open != close_keys[ch]:
                return False

    return False if bracket_stack else True


print(isValid("[{()}]}"))
