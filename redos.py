# 394 - decode string
# 8:47

"""
3[a]2[bc]
the format of this makes me think of using a stack
    we want to interpret the number until bracket opens
    then multiply everything inside of it
if number, add to temp, until open bracket, then add all of number to stack
if alpha, add to temp
if open bracket, add temp to stack
if closed bracket, multiply temp with stack

3[a2[c]]
"""


def decode_string(s):
    stack, temp, decoded = [], [], []
    idx = 0
    while idx < len(s):
        if s[idx].isnumeric():
            num_start = idx
            while s[idx].isnumeric():
                idx += 1
            if temp:
                stack.append("".join(temp))
                temp = []
        elif s[idx].isalpha():
            temp.append(s[idx])
            idx += 1
        elif s[idx] == "[":
            stack.append(s[num_start:idx])
            idx += 1
        elif s[idx] == "]":
            popped = stack.pop()
            if popped.isnumeric():
                temp = [int(popped) * "".join(temp)]
            else:
                temp = [popped + "".join(temp)]
            idx += 1
        print(stack, temp)
    return stack


s = "3[a2[c]]"
print(decode_string(s))


from collections import defaultdict


def course_list(numCourses, prerequisites):
    adj_list = defaultdict(list)
    in_degrees = defaultdict(int)

    for course, prereq in prerequisites:
        adj_list[prereq] = course
        in_degrees[course] += 1

    courses_taken = 0
    queue = []
    for course in range(numCourses):
        if in_degrees[course] == 0:
            queue.append(course)
            courses_taken += 1
    while queue:
        new_queue = []
        for course in queue:
            for postreq in adj_list[course]:
                in_degrees[postreq] -= 1
                if in_degrees[postreq] == 0:
                    new_queue.append(postreq)
                    courses_taken += 1
        queue = new_queue
    return True if courses_taken == numCourses else False


# 299 - Bulls and Cows

#  secret and guess - length between 1 and 1000
#  return hint as xAyB - x is digits in correct position, y is digits in wrong position

# at every idx, check if digit is the same - if yes, add to bulls (x), if no, add to dictionary with freq
# at the end - compare minimum freq of characters in guess

# from collections import defaultdict


def get_hint(secret, guess):
    bulls = cows = 0
    secret_ch, guess_ch = defaultdict(int), defaultdict(int)

    for idx in range(len(secret)):
        if secret[idx] == guess[idx]:
            bulls += 1
        else:
            secret_ch[secret[idx]] += 1
            guess_ch[guess[idx]] += 1

    for ch in guess_ch.keys():
        cows += min(secret_ch[ch], guess_ch[ch])

    return str(bulls) + "A" + str(cows) + "B"


# 20 - Valid Parentheses

# 1:35


def valid_parentheses(s):
    bracket_mapping = {"(": ")", "{": "}", "[": "]"}
    bracket_stack = []

    for br in s:
        if br in bracket_mapping:
            bracket_stack.append(br)
        elif bracket_stack and bracket_mapping[bracket_stack[-1]] == br:
            bracket_stack.pop()
        else:
            return False
    return not bracket_stack
