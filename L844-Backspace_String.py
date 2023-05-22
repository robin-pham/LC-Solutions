L844 - Backspace_String.py


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_typed, t_typed = [], []
        for ch in s:
            if ch.isalpha():
                s_typed.append(ch)
            elif s_typed:
                s_typed.pop()
            else:
                continue
        for ch in t:
            if ch.isalpha():
                t_typed.append(ch)
            elif t_typed:
                t_typed.pop()
            else:
                continue
        return s_typed == t_typed

    # time, space O(N)
