#!/usr/bin/python3

def remove_char_at(str, n):
    """A function removing the character at the position n

	Args:
		str: string
		n: position
    Returns:
        new string
    """
    if n >= 0:
        str = str[0:n] + str[n + 1:]
        return str
    else:
        return str
