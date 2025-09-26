import sys
import base64
import sys


def base64_tohex(base64_string):
    try:
        padded_base64_string = base64_padding(base64_string)
        decoded_bytes = base64.b64decode(padded_base64_string)
        return decoded_bytes.hex()
    except Exception as e:
        return f"Error decoding Base64: {e}"
        
def hex_to_base64(hex_string):
    try:
        if len(hex_string) % 2 != 0:
            hex_string = "0" + hex_string
        bytes_data = bytes.fromhex(hex_string)
        return base64.b64encode(bytes_data).decode('utf-8')
    except Exception as e:
        return f"Error converting Hex to Base64: {e}"

def base64_padding(base64_string):
    try:
        padding = ((4 - len(base64_string) % 4) % 4)
        padded_string = base64_string + ("=" * padding)
        return padded_string
    except Exception as e:
        return f"Error padding Base64 string: {e}" 
       
