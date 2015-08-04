#!/usr/bin/python2

import ulamspiral

limit = 700

def primes_range(stop):
    """ Form a prime sieve and return a list of primes below 'stop'."""
    primes = [True] * stop
    primes[0], primes[1] = [False] * 2
    L = []
    for ind, val in enumerate(primes):
        if val:
            primes[ind*2::ind] = [False] * (((stop - 1)//ind) - 1)
            L.append(ind)
    return L

# Form the Ulam Spiral
S = ulamspiral.UlamSpiral(limit)

# Form the list of primes
P = set(primes_range(limit))

# Show only primes in the spiral
# Determine character width for printing                                                       
char_width = len(str(max([max(i) for i in S.rows]))) + 1
for row in S.rows:
    row_str = ''
    for i in row:
        if i <= S.max_int and i in P:
            row_str += str(i).rjust(char_width)
        else:
            row_str += ''.rjust(char_width)
    print row_str

