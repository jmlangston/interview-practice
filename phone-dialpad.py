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


def dialpad(nums):

    list_letters = []

    for num in nums:
        list_letters.append(dialpad_dict[num])

    combos_list = []

    prefixes = list_letters[0]

    for prefix in prefixes:
        for letter in list_letters[1]:
            combo = prefix + letter
            combos_list.append(combo)

    print combos_list


dialpad('79')
