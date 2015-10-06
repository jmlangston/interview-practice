# given one or more numbers (0-9) write a function that returns a list of all combinations of letters that these numbers could make on a standard phone dialpad

# ex: '2' -> ['A', 'B', 'C']
# ex: '23' -> ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']

dialpad_dict = {
    '0': '',
    '1': '',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}


combos_list = []

i = 0


def dialpad(nums, combos_list, i):

    while i < len(nums):


    for num in nums:


    # list_letters = []

    # for num in nums:
        # list_letters.append(dialpad_dict[num])

    # print list_letters

    # for letters in list_letters:
    #     for letter in letters:
    #         print letters[]

    # for i in range(len(list_letters)):
    #     letters = list_letters[i]
    #     for j in range(len(letters)):
    #         combo = i + j
    #         combos_list.append(combo)

    print combos_list


# dialpad('23')
