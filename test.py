def morse(text):
    if not isinstance(text, str):
        raise ValueError("Invalid input. Only strings are allowed.")
    
    morse_code = {
        'A': '.-', 'Á': '.--.-', 'B': '-...', 'C': '-.-.', 'Č': '-.-..', 'D': '-..', 'Ď': '-..-', 'E': '.', 'É': '..-..', 'Ě': '..-..', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'Í': '..-..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ň': '--.--', 'O': '---', 'Ó': '---.', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'Ř': '.-.-', 'S': '...', 'Š': '...-', 'T': '-', 'Ť': '-.-.', 'U': '..-', 'Ú': '..--', 'Ů': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Ý': '-.--.', 'Z': '--..', 'Ž': '--..-',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    }
    
    morse_text = ''
    for char in text.upper():
        if char.isalnum():
            if char in morse_code:
                morse_text += morse_code[char] + '/'
        else:
            raise ValueError(f"Invalid character: {char}")
    return morse_text.strip('/')

# Example usage
text = "Hello World"
morse_text = morse(text)
print(morse_text)
