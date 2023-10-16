# 494 - Target Sum

"""
given int array and an int target - you want to build expression of numbers by adding or subtracting each num
return number of different expressions that can be build that evaluates to target

len of nums is 1<= x <= 20
sum 0 <= x <= 1000
target -1000 <= x <= 1000
nums[i] 0 <= x <= 1000
so if we just check all combinations of +/- -> that's 2**20 which is 1 million possibilities
is there a nicer way to do this?
"""


# time limit exceeded on this at test case 75/140 - [40,21,33,25,8,20,35,9,5,27,0,18,50,21,10,28,6,19,47,15]
# memoize idx and current sum! all the possible current sums at the index are kept, then redundant paths aren't traced?
# or how do we get the end results o the redundant path?
def target_sum(nums, target):
    def combinations(sum, idx):
        if (sum, idx) in memo:
            return memo[(sum, idx)]
        if idx == len(nums):
            if sum == target:
                memo[(sum, idx)] = 1
            else:
                memo[(sum, idx)] = 0
        else:
            plus = combinations(sum + nums[idx], idx + 1)
            minus = combinations(sum - nums[idx], idx + 1)
            memo[(sum, idx)] = plus + minus

        return memo[(sum, idx)]

    memo = {}
    x = combinations(0, 0)
    print(sorted(memo.items()))
    return x


nums = [40, 21, 33, 25, 8, 20, 35]
print(target_sum(nums, 3))
