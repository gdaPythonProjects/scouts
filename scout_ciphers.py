def cesar(input_string, shifts = 13):
    chars = list(input_string.upper())

    for char in chars:
        number_in_ascII = ord(char)

        if number_in_ascII < 65 or number_in_ascII > 90:
            return ('Input string should contain only a-z Latin alphabet letters'
            '(no special signs or numbers!) without white-spaces.')

        index = chars.index(char)
        number_in_ascII += shifts

        if number_in_ascII > 90:
            number_in_ascII = (number_in_ascII - 90) + 65

        char = chr(number_in_ascII)
        chars[index] = char

    return ''.join(chars)
