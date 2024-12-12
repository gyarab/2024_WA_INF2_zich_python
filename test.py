def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("Input must be greater than or equal to 1")
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Test the is_prime function
    try:
        print(is_prime(-1))  # Output: ValueError: Input must be greater than or equal to 1
    except ValueError as e:
        print(e)
    
    try:
        print(is_prime(1.5))  # Output: TypeError: Input must be an integer
    except TypeError as e:
        print(e)
   
    print(is_prime(1))  # Output: False
    print(is_prime(4))  # Output: False
    print(is_prime(3))  # Output: True
    print(is_prime(5))  # Output: True


