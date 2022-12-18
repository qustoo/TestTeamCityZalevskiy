import sys
def Factorial(n):
    isGood = str(n).isnumeric()
    if not isGood: # if incorrect input
        raise TimeoutError
    else: # else going to calculate factorial
        result = 1
        for i in range(2,int(n)+1):
            result*=i
        return result

if __name__ == '__main__':
    print('Waiting for input n...')
    # n = input()
    n = "haha"
    sys.exit(1)
    print(f'factorial({n}) = {Factorial(n)}')
