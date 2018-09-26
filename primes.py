# Live repl version: https://repl.it/@wrathofdon/Prime-Numbers

# The premise modify the Sieve of Eratosthenes to O(n) time

# In the original version, every non-prime can be crossed off multiple times
# for every prime factor.  6 is crossed off when 2 is multiplied by 3, then again
# when 3 is multiplied by 3.

# In this version, non-primes are only crossed off once, based on their largest
# prime factor, removing the redunancy.


# program searches for all prime numbers <= input
size = int(input("What is the range you would like to search? "))

# divide array in half, each element represents an odd number.
array = [-1] * int((size + 1) / 2)

array[1] = 1;
n = len(array)
primes = [2, 3]
# the limit is the index of the largest prime factor for future consideration
# this is because you will no longer cross off multiples if the product exceeds
# the size of the array
limit = 1
# the limit should continue to grow until we reach the root of n
root = int((n * 2 + 2) ** .5)

for i in range(1, n):
    currentNum = (i * 2) + 1
    # Numbers that are -1 have not been "crossed off", and must therefore be prime
    if array[i] == -1:
        primes.append(currentNum)
        # once we pass the 1/3 mark, it will be impossible to cross off any new
        # numbers, because new numbers will be too big for the array
        if limit == 0:
            continue
        if primes[-1] <= root:
            limit += 1;
        # p represents the index of the prime numbers, starting at 3 (index 1)
        # the limit is there so we don't bother with products that we already
        # know will be too big
        for p in range(1, limit + 1):
            index = int(((currentNum * primes[p]) - 1) / 2)
            # if the product is too big, then we need to reduce the limit
            if index >= n:
                limit = p
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
                limit = p
                break
            array[index] = p
print(primes)
