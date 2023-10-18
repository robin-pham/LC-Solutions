# 31 - Next permutation



# go through the array in reverse - find the first instance of a number[i] > number[i-1] 
#   if you find this, take number[i:] and place it in front of number[i-1]

# [1,6,5,4] -> [4,1,5,6] - found 1 and 6 - 4 goes in front, 5 and 6 sorted

#  [1,6,3,8,9,2] -> [1,6,3,9,2,8]  - found 9 and 8

#  [4,6,5,3] -> [5, 3,4,6]  - found 6 and 4 - but 5 goes in front, then the rest are sorted
