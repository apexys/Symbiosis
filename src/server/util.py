def slurp(filename):
    with open(filename, 'r') as slurpfile:
        data = slurpfile.read()
    return data
