#  136 - Single Number

# 9:46 
# time O(N) and extra space O(1) :o

# ok wtf
# the xor operation (^) works like this:
# if you xor 0 and x: 0^x = x
# if you xor x and x: x^x = 0
# so x^y^z^x^y = (x^x)^(y^y)^z = 0^z = z

def single_number(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor

nums = [1,1,5,7,3,8,4,7,8,5,3]
print(single_number(nums))