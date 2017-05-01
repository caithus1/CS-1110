# Christopher Geier (cpg3rb)
int_integer = int(input('Enter an integer: '))
if 0 < int_integer < 4000:
    numerals, steps, roman, integer = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'], \
                                      [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1], '', int_integer + 1
    for b in range(0, len(steps)):
        while integer - steps[b] > 0:
            integer -= steps[b]
            roman += numerals[b]
    print('In roman numerals, ' + str(int_integer) + ' is ' + roman)
else:
    print('Input must be between 1 and 3999')
