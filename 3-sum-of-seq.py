def get_sum(a,b):
    sum = 0
    for i in range(min(a,b), max(a,b) + 1):
        sum = sum + i
    return(sum)

print(get_sum(0,-10))

# Given two integers a and b, which can be positive or negative,
# find the sum of all the numbers between including them too and return it.
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!
