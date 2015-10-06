def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into its decimal equivalent.

#         >>> hex_convert('6')
#         6

#         >>> hex_convert('10')
#         16

#         >>> hex_convert('FF')
#         255

#         >>> hex_convert('FFFF')
#         65535
# """

    alpha_dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    nums = []

    power = 0

    for c in reversed(hex_in):
        if c.isalpha() is True:
            c = alpha_dict[c]
        nums.append(int(c) * (16 ** power))
        power += 1

    return sum(nums)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. YOU'RE TERRIFIC! ***\n"
