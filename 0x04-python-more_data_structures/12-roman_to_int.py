#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == "" or not isinstance(roman_string, str):
        return 0
    new1 = {'I': 1, 'II': 2, 'III': 3, 'IV': 4,
            'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}
    new2 = {'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40,
            'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90}
    new3 = {'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400,
            'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900}
    new4 = {'M': 1000, 'MM': 2000, 'MMM': 3000}
    sum = 0
    if 'IV' in roman_string:
        a = roman_string.index('IV')
        sum += new1[roman_string[a:]]
        roman_string = roman_string[:a]
    if 'V' in roman_string:
        a = roman_string.index('V')
        sum += new1[roman_string[a:]]
        roman_string = roman_string[:a]
    if 'I' in roman_string:
        b = roman_string.index('I')
        sum += new1[roman_string[b:]]
        roman_string = roman_string[:b]

    if 'XL' in roman_string:
        a = roman_string.index('XL')
        sum += new2[roman_string[a:]]
        roman_string = roman_string[:a]
    if 'L' in roman_string:
        a = roman_string.index('L')
        sum += new2[roman_string[a:]]
        roman_string = roman_string[:a]
    if 'X' in roman_string:
        b = roman_string.index('X')
        sum += new2[roman_string[b:]]
        roman_string = roman_string[:b]

    if 'CD' in roman_string:
        a = roman_string.index('CD')
        sum += new3[roman_string[a:]]
        roman_string = roman_string[:a]
    if 'D' in roman_string:
        a = roman_string.index('D')
        sum += new3[roman_string[a:]]
        roman_string = roman_string[:a]
    if 'C' in roman_string:
        b = roman_string.index('C')
        sum += new3[roman_string[b:]]
        roman_string = roman_string[:b]

    if 'M' in roman_string:
        b = roman_string.index('M')
        sum += new4[roman_string[b:]]
        roman_string = roman_string[:b]
    return sum
