def Factorial(n):
    result = 1
    for i in range(2,n+1):
        result*=i
    return result

if __name__ == '__main__':
    print('Waiting for input n...')
    n = int(input())
    print(f'factorial({n}) = {Factorial(n)}')
