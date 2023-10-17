def intToRoman(num: int) -> str:
    simb = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
            90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
            1: 'I'}
    s = ''
    for key, val in simb.items():
        while num > key:
            s = s + simb[key]
            num -= key
    return s


print(intToRoman(1994))