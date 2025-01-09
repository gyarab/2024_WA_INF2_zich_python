def primes_in_range(a, b):
    primes = []
    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, int(num/2) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

if __name__ == "__main__":
    result = primes_in_range(1, 100)
    print(result)