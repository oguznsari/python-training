def find_it(seq):
    for i in seq:
        count = seq.count(i)
        if count % 2 != 0:
            return(i)

seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4, -1,-2,9]
print(find_it(seq))

# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
