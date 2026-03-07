import pytest

def word_order(string):
    wordList= string.split('-')
    orderedList= sorted(wordList)
    end_up='-'.join(orderedList)
    return end_up

if __name__ == "__main__":
    end_up = word_order('python-variable-funcion-computadora-monitor')
    print(end_up)