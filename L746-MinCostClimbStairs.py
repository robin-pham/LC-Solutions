# 746 - Min Cost Climbing Stairs

"""
int array cost - where cost[i] is cost of stepping on staircase
when you pay cost, you can climb 1 or 2 steps
can start on step 0 or 1
min cost

cost length 2<= x <= 1000
cost 0 <= x <= 999

seems like a top down type approach, where cost at i = cost[i] + min(fun(i-1), fun(i-2))
"""


def min_cost(cost):
    def cost_at_step(idx):
        if idx in step_memo:
            return step_memo[idx]
        if idx < 0:
            return 0
        elif idx == 0:
            return cost[0]
        elif idx == 1:
            return cost[1]
        else:
            min_answer = cost[idx] + min(cost_at_step(idx - 1), cost_at_step(idx - 2))
            step_memo[idx] = min_answer
            return min_answer

    step_memo = {}
    return min(cost_at_step(len(cost) - 1), cost_at_step(len(cost) - 2))


cost = [10, 15, 20]
print(min_cost(cost))
