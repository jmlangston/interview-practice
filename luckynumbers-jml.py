# hackbright coding challenge "lucky numbers"

# given the numbers 1-10 (inclusive), return a list of n random numbers, making sure to never return a number more than once. this function will never be called with n < 0 or n > 10. this function may be called with 0.


# solution 1 - my first solution

import random

def lucky_nums_1(n):
    """Returns n random integers between 1-10."""

    list_randoms = [] #O(1)
    while len(list_randoms) < n: #O(n)
        random_num = random.randint(1, 10) #O(1)
        if random_num in list_randoms: #O(n)
            continue
        else:
            list_randoms.append(random_num) #O(1)
    return list_randoms #O(1)

# runtime:  O(n^2) ?
# space:    ?


# solution 2 - my solution using a set

def lucky_nums_2(n):

    set_randoms = set([]) #O(1)
    while len(set_randoms) < n: #O(n) ?
        random_num = random.randint(1, 10) #O(1)
        set_randoms.add(random_num) #O(1)
    return set_randoms #O(1)

# runtime:  O(n) ?
# space:    ?
# but i don't think the runtime is right because the while loop may be iterated over more than n times (i.e. if the randint is already in the set)


# solution 3 - with random.choice()

def lucky_nums_3(n):

    nums = range(1,11) #O(1) ? O(len(range)) ?
    lucky_nums = [] #O(1)

    for i in range(n): #O(n)
        num = random.choice(nums) #O(1)
        nums.remove(num) #O(1)
        lucky_nums.append(num) #O(1)

    return lucky_nums #O(1)

# runtime:  O(n) ?
# space:    ?

# solution 4 - with random.sample()

def lucky_nums_4(n):

    return random.sample(range(1,11), n)

# runtime:  ?
# space:    ?
