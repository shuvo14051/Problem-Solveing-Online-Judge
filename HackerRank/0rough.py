def remove_extra_spaces(s):
    # Split the string into words
    words = s.split()

    # Join the words back together with a single space
    result = ' '.join(words)

    return result


print(remove_extra_spaces("hello   world  lol"))