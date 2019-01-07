def cesar(input_string, shifts=13):
    if isinstance(input_string, str) is False or input_string is '':
        raise ValueError('input_string should be type of str() and not empty or null')
    if isinstance(shifts, int) is False or shifts <= 0:
        raise ValueError('shifts should be type of int() and greater then zero')
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
        raise ValueError('input_string should be type of str() and not empty or null')
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
