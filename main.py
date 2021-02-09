import math


def divisors(n):
    d = []
    s = int(math.sqrt(n))
    for x in range(1, s+1):
        if n % x == 0:
            d.append(x)
            d.append(int(n/x))
    d = list(set(d))
    d.sort()
    return d


def force_integer(string):
    while True:
        try:
            n = int(string)
            if n < 0:
                raise ValueError
            break
        except ValueError:
            string = input('Must be non-negative integer. Try again: ')
    return string


def is_abundant(n):
    return bool(sum(divisors(n)) > 2*n)


def abundant_list(m):
    i = 0
    n = 1
    abundants = []
    while i < m:
        if is_abundant(n):
            abundants.append(n)
            i += 1
        n += 1
    return abundants


def is_prime(n):
    return bool(len(divisors(n)) == 2)


def prime_list(m):
    i = 0
    n = 1
    primes = []
    while i < m:
        if is_prime(n):
            primes.append(n)
            i += 1
        n += 1
    print(primes)


def menu():
    s = ['prime', 'abundant']
    f_list = [is_prime, is_abundant]
    g_list = [prime_list, abundant_list]
    sequence_menu = 'What sequences are you interested in?\n'
    for i in range(len(s)):
        sequence_menu += str(i+1) + '. ' + s[i].capitalize() + ' Numbers\n'
    x, y = '', ''
    while x not in range(1, len(s)+1):
        x = int(force_integer(input(sequence_menu)))
    while y not in [1, 2]:
        y = int(force_integer(input('Which would you like to do?\n'
                  '1. Check a specific number\n'
                  '2. Get a list of the first n such numbers\n'
                  'Enter your selection in integer form:\n')))
    if y == 1:
        c = int(force_integer(input('Enter your integer:\n')))
        f = f_list[x-1]
        if f(c):
            print(c, 'is ' + s[x-1] + '.')
        else:
            print(c, 'is not ' + s[x-1] + '.')
    if y == 2:
        m = int(force_integer(input('How many results would you like?\n')))
        g = g_list[x-1]
        print('The first ' + str(m) + ' ' + s[x-1] + ' numbers are:\n', g(m))


if __name__=='__main__':
    menu()




