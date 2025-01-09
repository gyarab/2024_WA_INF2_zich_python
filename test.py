def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("Input value must be a string.")
    parts = []
    for i in range(0, len(text), 3):
        parts.append(text[i:i+3])
    return parts

if __name__ == "__main__":
    print(split_into_threes(123))
