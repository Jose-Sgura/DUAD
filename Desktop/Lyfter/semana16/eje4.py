import pytest

def backingoff(string):
    return string[::-1]
    
if __name__ == "__main__":
    structure = backingoff('Hola Mundo')
    print('The word backwards is-----'  + structure)

