# Love Encoder

A simple Python library for encoding strings based on a predefined mapping, with constant random characters for both uppercase and lowercase letters. Make by lovevsick

## Installation

You can install the library using pip:

```bash
pip install love_encoder

*
from love_encoder import encode_string, decode_string

input_text = "Hello World"
encoded_text = encode_string(input_text)
print(f"Encoded '{input_text}' to '{encoded_text}'")

decoded_text = decode_string(encoded_text)
print(f"Decoded '{encoded_text}' back to '{decoded_text}'")

If you have any scripts that import from `custom_encoder`, make sure to change those imports to `love_encoder`:

```python
from love_encoder import encode_string, decode_string

input_text = "Hello World"
encoded_text = encode_string(input_text)
print(f"Encoded: {encoded_text}")

decoded_text = decode_string(encoded_text)
print(f"Decoded: {decoded_text}")
*