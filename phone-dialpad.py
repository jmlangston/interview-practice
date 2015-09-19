# given one or more numbers (0-9) write a function that returns a list of all combinations of letters that these numbers could make on a standard phone dialpad

# ex: '2' -> ['ABC']
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


def dialpad(nums):

    combos_list = []

    list_letters = []
    for num in nums:
        list_letters.append(dialpad_dict[num])

    # for letters in list_letters:
    #     for letter in letters:
    #         print letters[]

    # for i in range(len(list_letters)):
    #     letters = list_letters[i]
    #     for j in range(len(letters)):
    #         combo = i + j
    #         combos_list.append(combo)

    print combos_list


dialpad('23')
