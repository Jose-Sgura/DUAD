import pytest

def sum(pist):
    plus=0
    for counter in pist:
        plus+=counter
    return plus
total=sum([4,6,2,29])
print(f'The sum result is {total}')

if __name__ == "__main__" :
    sum([4,6,2,29])