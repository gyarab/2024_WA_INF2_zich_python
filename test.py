def primes_in_range(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    if a > b:
        a, b = b, a
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
    result = primes_in_range(15, 9)
    print(result)