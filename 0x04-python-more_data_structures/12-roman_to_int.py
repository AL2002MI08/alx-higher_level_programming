#!/usr/bin/python3

def roman_to_int(roman_string):
    """Coverts a roman numeral to an integer"""
    sum_num = 0
    roman_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0

    roman_len = len(roman_string)
    for x in range(roman_len):
        if roman_num.get(roman_string[x], 0) == 0:
            return 0

        if (x != (roman_len - 1) and
                roman_num[roman_string[x]] < roman_num[roman_string[x + 1]]):
            sum_num += roman_num[roman_string[x]] * -1
        else:
            sum_num += roman_num[roman_string[x]]
    return sum_num
