# 22 - Generate Parentheses
#  2:51 4:21
'''
n = 1
()

n=2
()
then
0    (())   surround all
1    ()()   add idx 0

n=3
0   (()), (()())
1   ()(())         add idx 0
1   (())()         add idx 4
2   ()()()         add idx 0

n=4
nest all - ((())), ((()())), (()(())), ((())()), (()()())
add to every index - ()(()), (())(), ()(()()), (()())(),  ()()(())


combo: make current combo, pass it forward and do all the possible operations on it
        -in certain cases, do not do some operations 
        i think we can carry eveyrthing forward except if its in a memo
-add () to every index
-
'''


# def generate_parentheses(n):
#     level_memo = [set() for _ in range(n+1)]
#     level_memo[1].add('()')
#     def make_combo(current, n):
#         nonlocal level_memo
#         current_level = len(current)//2 + 1
#         if current_level > n:
#             return
#         for idx in range(len(current)+1):
#             new_combo = current[:idx] + '()' + current[idx:]
#             if new_combo not in level_memo[current_level]:
#                 level_memo[current_level].add(new_combo)
#                 make_combo(new_combo, n)

#     make_combo('()', n)
#     return list(level_memo[n])

# print(generate_parentheses(4))



# second solution
def generate_parentheses(n):
    combos = []

    def make_combo(current, left, right, n):
        print(current, left, right)
        nonlocal combos
        if left+right == n*2:
            combos.append(current)
            return
        if left == n:
            make_combo(current+')', left, right+1, n)
        elif left == right:
            make_combo(current+'(', left+1, right, n)
        else:
            make_combo(current+'(', left+1, right, n)
            make_combo(current+')', left, right+1, n)

    make_combo('', 0, 0, n)
    return combos

print(generate_parentheses(4))

        # if left == right, add '(', else, add both adn call f
        












