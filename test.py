def morse(text):
    if not isinstance(text, str):
        raise ValueError("Invalid input. Only strings are allowed.")
    
    morse_code = {
        'A': '.-', 'À': '.-', 'Á': '.-', 'Â': '.-', 'Ã': '.-', 'Ä': '.-', 'Å': '.-', 'Æ': '.-', 'Ç': '-.-.', 'D': '-..', 'E': '.', 'È': '.', 'É': '.', 'Ê': '.', 'Ë': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'Ì': '..', 'Í': '..', 'Î': '..', 'Ï': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '-.', 'O': '---', 'Ò': '---', 'Ó': '---', 'Ô': '---', 'Õ': '---', 'Ö': '---', 'Ø': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'Ù': '..-', 'Ú': '..-', 'Û': '..-', 'Ü': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Ý': '-.--', 'Ÿ': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
    }
    
    morse_text = ''
    for char in text.upper():
        if char in morse_code:
            morse_text += morse_code[char] + '/'
        else:
            raise ValueError(f"Invalid character: {char}")
    
    return morse_text.strip('/')

# Example usage
text = "Hello World"
morse_text = morse(text)
print(morse_text)
