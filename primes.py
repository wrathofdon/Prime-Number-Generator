# Live repl version: https://repl.it/@wrathofdon/Prime-Numbers

# The premise of this program is to make the Sieve of Eratosthenes more efficient

# In the original version, every time you find a prime number, you cross off all
# multiple of those primes.  The inefficiency happens because the same number
# can be crossed off multiple times based ont he number of prime factors.
# 15 will be crossed off when you discover 3 is a prime and multiply by 5, but
# it will also be crossed off when you discover 5 is a prime and multiply by 3

# In this version, every number is only crossed off once, because crossing off
# only happens when the prime factors are in a specific order.

# Newly discovered prime numbers will cross off the product they have with all
# other prime numbers smaller than itselfself.  5 * 3 is valid, but 3 * 5 is not.

# Non-prime numbers will be cross off the product they have with all prime
# prime numbers equal to or bigger than it's largest prime factor

# i.e., 27's biggest prime factor is 3.  It will cross off itself multiplied by
# 3 (81), 5 (135), 7 (189), 9 (243), 11, 13, 17, 19, and 23.

# 14's biggest prime factor is 7.  It will skip past 3 and 5.
# It will only be multiplied by 7 (98), 11 (154), and 13 (182).

# program searches for all prime numbers <= input
size = int(input("What is the range you would like to search? "))

# divide array in half, because we only care about odd numbers
# An array of length 10 would represent all odd numbers from 0 - 19.
# To convert from the index to the number it represents, multiply * 2 and add 1
# i.e., index 0 represents 1, index 1 represents 3, index 2 represents 5, etc.
array = [-1] * int((size + 1) / 2)

array[1] = 1;
n = len(array)
primes = [2, 3]
# the limit is the index of the largest prime factor for future consideration
limit = 1

for i in range(1, n):
    currentNum = (i * 2) + 1
    # if array[i] is still -1, then it means it has not been crossed off
    # this also means that it must be a prime
    if array[i] == -1:
        primes.append(currentNum)
        # once we pass the 1/3 mark, it will be impossible to cross off any new
        # numbers, because new numbers will be too big for the array
        if limit == 0:
            continue
        # if the current prime is equal to a smaller than the root of n, then
        # we can expand the number of primes we multiply.  If it's bigger than
        # the root, then all future products will be too big for the array
        if primes[-1] <= int((n * 2 + 1) ** .5):
            limit += 1;
        # p represents the index of the prime numbers, starting at 3 (index 1)
        # the limit is there so we don't bother checking multiples when we
        # already know that the number is too big
        for p in range(1, limit + 1):
            index = int(((currentNum * primes[p]) - 1) / 2)
            # if the product is too big, then we need to reduce the limit
            # if currentNum * x is too big, then all future numbers * x will
            # also be too big.
            if index >= n:
                limit = p - 1
                break
            # otherwise, we "cross off" the number by marking it with the index
            # of it's largest prime factor.
            array[index] = p
    else:
        # if the element value != -1, then it represents the index of its
        # largest prime factor.  i.e., if you see a '1', then the largest prime
        # factor would be 3.
        for p in range(array[i], limit):
            index = int(((currentNum * primes[p]) - 1) / 2)
            if index >= n:
                limit = p - 1
                break
            array[index] = p
print(primes)
