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


def gaderypoluki(input_string, key):
    if isinstance(input_string, str) is False or input_string is '':
        raise ValueError('input_string should be type of str() and not empty or null')
    if isinstance(key, str) is False or key is '':
        raise ValueError('key should be type of str() and not empty or null')

    input_string = input_string.lower()
    key = key.lower()

    i = 2
    while i < len(key):
        if key[i] is not '-':
            raise ValueError("Wrong format of key value. Should be like: 'GA-DE-RY-PO-LU-KI'")
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
