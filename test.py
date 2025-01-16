def caesar_encode(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    encoded_text = ""
    for char in text:
        if char.isalpha() and char.isascii():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encoded_char = chr((ord(char) - ascii_offset + 3) % 26 + ascii_offset)
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

def caesar_decode(code):
    decoded_text = ""
    for char in code:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - ascii_offset - 3) % 26 + ascii_offset)
            decoded_text += decoded_char
        else:
            decoded_text += char
    if not decoded_text.isalpha():
        raise ValueError("Invalid code")
    return decoded_text



