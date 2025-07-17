import base64

def base64_tohex(base64_string):
    try:
        decoded_bytes = base64.b64decode(base64_string)
        return decoded_bytes.hex()
    except Exception as e:
        return f"Error decoding Base64: {e}"
    
def hex_to_base64(hex_string):
    try:
        bytes_data = bytes.fromhex(hex_string)
        return base64.b64encode(bytes_data).decode('utf-8')
    except Exception as e:
        return f"Error converting Hex to Base64: {e}"