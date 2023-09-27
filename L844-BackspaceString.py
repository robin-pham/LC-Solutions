def string_compare(s, t):
    s_stack = []
    t_stack = []

    for ch in s:
        if ch.isalpha():
            s_stack.append(ch)
        elif s_stack:
            s_stack.pop()

    for ch in t:
        if ch.isalpha():
            t_stack.append(ch)
        elif t_stack:
            t_stack.pop()

    return s_stack == t_stack


s = "a#c"
t = "b"
print(string_compare(s, t))
