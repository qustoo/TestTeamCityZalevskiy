def Factorial(n):
    isGood = str(n).isnumeric()
    if not isGood: # if incorrect input
        return None
    else: # else going to calculate factorial
        result = 1
        for i in range(2,int(n)+1):
            result*=i
        return result

def test_error():
    pass
    # n = Factorial(5)
    # assert n == 20

if __name__ == '__main__':
    print('Waiting for input n...')
    n = input()
    print(f'for n ={n}, factorial = {Factorial(n)}')
