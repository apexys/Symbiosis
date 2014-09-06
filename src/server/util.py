def slurp(filename):
    with open(filename, 'r') as slurpfile:
        data = slurpfile.read()
    return data

def spit( filename, contents ):
    with open( filename, 'w' ) as spitfile:
        spitfile.write( contents )
