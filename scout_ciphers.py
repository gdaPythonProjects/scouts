def cesar(input_string, shifts=13):
    if isinstance(input_string, str) is False or input_string is None or input_string is '':
        raise ValueError('input_string should be type of str() and not empty or null')
    if isinstance(shifts, int) is False or shifts <= 0:
        raise ValueError('shifts should be type of int() and bigger then zero')
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
