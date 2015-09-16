# in: integer
# out: roman numeral equivalent

def convert_roman_numeral_1(num):
    """Convert an integer into its Roman Numeral equivalent.

    Straight conversion by digits, so no substitution, so for example 9 would be VIIII instead of IX. Next attempt - with substitution.

    Example: 32 converts to XXXII

    >>> convert_roman_numeral_1(32)
    'XXXII'

    >>> convert_roman_numeral_1(9)
    'VIIII'

    """

    # make sure num is an integer
    num = int(num)

    roman_numeral = ''

    while num > 0:
        if num >= 1000:
            roman_numeral += 'M'
            num -= 1000
            continue
        if num >= 500:
            roman_numeral += 'D'
            num -= 500
            continue
        if num >= 100:
            roman_numeral += 'C'
            num -= 100
            continue
        if num >= 50:
            roman_numeral += 'L'
            num -= 50
            continue
        if num >= 10:
            roman_numeral += 'X'
            num -= 10
            continue
        if num >= 5:
            roman_numeral += 'V'
            num -= 5
            continue
        if num >= 1:
            roman_numeral += 'I'
            num -= 1
            continue

    return roman_numeral


# working on - a solution using a dictionary or other data structure

# def convert_roman_numeral_2(num):

#     rn_dict = {
#         '1000': 'M',
#         '500': 'D',
#         '100': 'C',
#         '50': 'L',
#         '10': 'X',
#         '5': 'V',
#         '1': 'I'
#     }

#     roman_numeral = ''

#     while num > 0:
#         for key in rn_dict:
#             if num >= key:
#                 roman_numeral += rn_dict[key]
#                 num -= key

#     return roman_numeral


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. GREAT JOB! ***\n"
