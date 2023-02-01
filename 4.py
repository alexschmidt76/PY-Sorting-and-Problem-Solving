def sort_alph(string):
    return sorted(string.split(' '), key=str.lower)
print(sort_alph('I love software engineering'))

