# integer-sequences
Integer-sequences is a simple program. It is built to generate different integer sequences and to tell you if
 integers are in those sequences.
 
## Motivation
Integer-sequences is just for fun. The aim is to avoid using powerful modules to generate these sequences. 

The math module is used where it offers simple, obvious, and powerful efficiency improvements, like using math.sqrt()
 as an upper bound when factoring numbers. 

## Current Offerings
As of February 8, 2021, integer-sequences covers the followings lists:
1. [Prime Numbers](https://en.wikipedia.org/wiki/Prime_number) ([OEIS A000040](https://oeis.org/A000040))
2. [Abundant Numbers](https://en.wikipedia.org/wiki/Abundant_number) ([OEIS A005101](https://oeis.org/A005101))
3. [Mersenne Primes](https://en.wikipedia.org/wiki/Mersenne_prime)([OEIS A000668](http://oeis.org/A000668))

*See Current Limitations (below)
## Installation
Install via git:
```bash
git clone https://github.com/coldbrewdev/integer-sequences
```

## Usage Example
$ python3 main.py

What sequences are you interested in?
1. Prime Numbers
2. Abundant Numbers
>2

Which would you like to do?
1. Check a specific number
2. Get a list of the first n such numbers
Enter your selection in integer form:
>2

How many results would you like?
>5

The first 5 abundant numbers are:

[12, 18, 20, 24, 30]

## Current Limitations
All the lists are subject to normal computational constraints, but when lists *quickly* become too complex, we
 restrict the code and list the limitation here. The limitation can be removed by modifying the code.
### Mersenne Primes
The function can only list the first eight (8) Mersenne Primes. Performance of the is_prime function seriously
 degrades beyond that point.