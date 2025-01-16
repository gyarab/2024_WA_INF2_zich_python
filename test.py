from unidecode import unidecode

def morse(text):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
    }
    
    morse_text = ''
    for char in unidecode(text.upper()):
        if char in morse_code:
            morse_text += morse_code[char] + ' '
    
    return morse_text.strip()

# Example usage
text = "Hello World"
morse_text = morse(text)
print(morse_text)