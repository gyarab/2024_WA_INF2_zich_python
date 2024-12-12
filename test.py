def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Test the is_prime function
    print(is_prime(5))  # Output: True
    print(is_prime(10))  # Output: False
    print(is_prime(17))  # Output: True
  


