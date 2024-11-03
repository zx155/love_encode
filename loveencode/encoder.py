encoding_map = {
    'a': 'gagiejh', 'A': 'gagiejh',
    'b': 'gt2y4h98', 'B': 'gt2y4h98',
    'c': 'f48ujg',  'C': 'f48ujg',
    'd': 'gu248990', 'D': 'gu248990',
    'e': 'gi8u24gov', 'E': 'gi8u24gov',
    'f': 'llaq1t',  'F': 'llaq1t',
    'g': 'g9q3p8',  'G': 'g9q3p8',
    'h': ';;;[qrf1', 'H': ';;;[qrf1',
    'i': ']][q.-0', 'I': ']][q.-0',
    'j': 'hu24hprw', 'J': 'hu24hprw',
    'k': '][poiuhn', 'K': '][poiuhn',
    'l': 'zxcvbefgqwe', 'L': 'zxcvbefgqwe',
    'm': 'awedx',   'M': 'awedx',
    'n': 'ghwer',   'N': 'ghwer',
    'o': '12474',   'O': '12474',
    'p': '(nP!~X',  'P': '(nP!~X',
    'q': 'gq1gi89', 'Q': 'gq1gi89',
    'r': 'lljqu',   'R': 'lljqu',
    's': '781h~',   'S': '781h~',
    't': '98efgb',  'T': '98efgb',
    'u': 'gihy82w', 'U': 'gihy82w',
    'v': "';w;lfa", 'V': "';w;lfa",
    'w': 'wwi1tg',  'W': 'wwi1tg',
    'x': 'gaqgwoo', 'X': 'gaqgwoo',
    'y': '5678kmbfe', 'Y': '5678kmbfe',
    'z': ',.a(*',   'Z': ',.a(*',
}

decoding_map = {v: k for k, v in encoding_map.items()}

def encode_string(input_string):
    """Encode the input string using the defined encoding map."""
    encoded_string = ''
    for char in input_string:
        if char in encoding_map:
            encoded_string += encoding_map[char]
        else:
            encoded_string += char  
    return encoded_string

def decode_string(encoded_string):
    """Decode the encoded string back to the original using the defined decoding map."""
    decoded_string = ''
    i = 0
    while i < len(encoded_string):
        # Check if any of the encoded values match the current position
        found = False
        for length in range(1, 20):  # Adjust the range based on max length of encoded values
            substring = encoded_string[i:i + length]
            if substring in decoding_map:
                decoded_string += decoding_map[substring]
                i += length
                found = True
                break
        if not found:
            decoded_string += encoded_string[i]  # Keep the character if not found
            i += 1
    return decoded_string