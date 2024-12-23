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
         # Output: ValueError: Input must be greater than or equal to 1
        print(is_prime(1))  # Output: False
         # Output: TypeError: Input must be an integer
        print(is_prime(4))  # Output: False
        print(is_prime(3))  # Output: True
        print(is_prime(5))  # Output: True   
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    
    


