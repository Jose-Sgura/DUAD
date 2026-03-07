import pytest

def qualifying_prime(number):
    if number<2:
        return False
    for index in range(2,int(number**0.5)+1):
        if number%index == 0:
            return False
    return True
def numberlist(enlist):
    prime=[]
    for n in enlist:
        if qualifying_prime(n):
            prime.append(n)
    return prime

if __name__ == "__main__":
    result = numberlist([1,4,6,7,13,9,67])
    print(result)