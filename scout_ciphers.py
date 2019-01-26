def shift_letter(char, shifts):
    if not isinstance(char, chr):
        raise ValueError('char should be typeof chr')
    if char == '' or char is None:
        raise ValueError('char should be typeof chr')
    if ord(char.upper()) < 65 or ord(char.upper()) > 90:
        raise ValueError('char should be only a-z Latin alphabet letters')

    char = char.upper()
    char = ord(char) + shifts
    char = char - 90 + 64 if char > 90 else char
    char = chr(char)
    return char


def cesar(input_string, shifts=13):
    if isinstance(input_string, str) is False or input_string is '':
        raise ValueError(
            'input_string should be type of str() and not empty or null')
    if isinstance(shifts, int) is False or shifts <= 0:
        raise ValueError(
            'shifts should be type of int() and greater then zero')
    if shifts is True or shifts is False:
        raise ValueError('shifts cannot be boolean value')

    chars = list(input_string.upper())
    encrypted_string = list()

    for char in chars:
        number_in_ascii = ord(char)

        if number_in_ascii < 65 or number_in_ascii > 90:
            raise ValueError('Input string should contain only a-z Latin alphabet letters'
                             '(no special signs or numbers!) without white-spaces.')

        number_in_ascii += shifts

        if number_in_ascii > 90:
            number_in_ascii = (number_in_ascii - 90) + 65

        char = chr(number_in_ascii)
        encrypted_string.append(char)

    return ''.join(encrypted_string)


def fence(input_string, fence_height):
    if isinstance(input_string, str) is False or input_string is '':
        raise ValueError(
            'input_string should be type of str() and not empty or null')
    if isinstance(fence_height, int) is False or fence_height < 2:
        raise ValueError('fence_height should be type of int greater then one')
    if isinstance(fence_height, bool):
        raise ValueError('fence_height cannot be typeof bool')

    fence_levels = list()

    i = 0
    while i < fence_height:
        fence_levels.append(list())
        i += 1

    level = 0
    go_down = True
    for sign in input_string:

        fence_levels[level].append(sign)

        if go_down:
            level += 1
        else:
            level -= 1

        if level == fence_height - 1:
            go_down = False
        if level == 0:
            go_down = True

    output_string = ''
    for lvl in fence_levels:
        for char in lvl:
            output_string += char

    return output_string


def gaderypoluki(input_string, key):
    if isinstance(input_string, str) is False or input_string is '':
        raise ValueError(
            'input_string should be type of str() and not empty or null')
    if isinstance(key, str) is False or key is '':
        raise ValueError('key should be type of str() and not empty or null')

    input_string = input_string.lower()
    key = key.lower()

    i = 2
    while i < len(key):
        if key[i] is not '-':
            raise ValueError(
                "Wrong format of key value. Should be like: 'GA-DE-RY-PO-LU-KI'")
        i += 3

    simplified_key = ''
    for char in key:
        if char is not '-':
            simplified_key += char

    output_string = ''
    for char in input_string:
        if char in simplified_key:
            index = simplified_key.index(char)
            if index % 2 is 0:
                index += 1
            else:
                index -= 1
            output_string += simplified_key[index]
        else:
            output_string += char

    return output_string


def vignere_table(i_row, i_column):
    table = [[chr(num) for num in range(65, 91, 1)]
             for c in range(65, 91, 1)]

    if not isinstance(i_row, int) or not isinstance(i_column, int):
        raise ValueError('i_row nad i_column should be typeof int')
    if i_row > 25:
        raise IndexError('i_rowe is out of range it should be below 26')
    if i_column > 25:
        raise IndexError('i_column is out of range it should be below 26')

    row = 1
    while row < len(table):
        column = 0
        while column < len(table[row]):
            letter = table[row][column]
            table[row][column] = shift_letter(letter, row)
            column += 1
        row += 1
    return table[i_row][i_column]


def vignere(input_string, key):
    if not isinstance(input_string, str):
        raise ValueError('Input string should be typeof str')
    if input_string is None or input_string is '':
        raise ValueError('Input string should be typeof str')

    input_string = input_string.upper()
    for c in input_string:
        if ord(c) < 65 or ord(c) > 90:
            if c is not ' ':
                raise ValueError(
                    'Input string should contain only a-z Latin alphabet letters')

    key = key.upper()
    correct_key = []

    i = 0
    for letter in input_string:
        if i == len(key):
            i = 0

        if letter == ' ':
            correct_key.append(letter)
        else:
            correct_key.append(key[i])
            i += 1

    correct_key = ''.join(correct_key)

    column = 0
    row = 0
    alphabet = [chr(i) for i in range(65, 91, 1)]
    output_string = []

    i = 0
    while i < len(input_string):
        if input_string[i] == ' ':
            output_string.append(input_string[i])
        else:
            column = alphabet.index(input_string[i])
            row = alphabet.index(correct_key[i])
            output_string.append(vignere_table(column, row))
        i += 1

    output_string = ''.join(output_string)
    return output_string
