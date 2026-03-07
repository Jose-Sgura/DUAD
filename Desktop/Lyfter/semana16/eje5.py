import pytest

def indentifier(text):
    capital=0
    lower=0
    for char in text:
        if char.isupper():
            capital+=1
        elif char.islower():
            lower+=1
    return capital, lower 

if __name__ == "__main__":
    capital, lower = indentifier('I love Nación Sushi')
    print(f'for the word ---I love Nación Sushi--- are {capital} upper cases and {lower} lower cases')