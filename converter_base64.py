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
       
def main():
    while True:
        try:
            print("Choose: ")
            print("1. Base64 to Hex")
            print("2. Hex to Base64")
            print("3. Exit")
            choice = input("Enter your choice (1, 2 or 3): ").strip()
        except ValueError:
            print('Invalid Option \n')

        if choice == '1':
            base64_string = input("Enter Base64 string: ").strip()
            hex_result = base64_tohex(base64_string)
            print(f"Hex result: {hex_result}")
        elif choice == '2':
            hex_string = input("Enter Hex string: ").strip()
            base64_result = hex_to_base64(hex_string)
            print(f"Base64 result: {base64_result}")
        elif choice == '3':
            print('Bye')
            sys.exit()
        elif choice == '0'or choice > '3':
            print('Invalid Option. Try Again \n')
        
        else:
            print("Invalid choice. Please enter 1 or 2.")      

if __name__ == "__main__":
    main()