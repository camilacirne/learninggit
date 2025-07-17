import base64
import sys
from converter_terminal import base64_tohex, hex_to_base64


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
    
def interactive_mode():
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
            print("Invalid choice. Please enter 1, 2 or 3.")   

def arg_way():
    if len(sys.argv) != 3:
        print("Use: python converter_terminal.py <Options> <string>")
        print("Options: b64tohex ou hextob64")
        sys.exit(1)

    options = sys.argv[1].lower()
    answers = sys.argv[2]

    if options == 'b64tohex':
        print(base64_tohex(answers))
    elif options == 'hextob64':
        print(hex_to_base64(answers))
    else:
        print("Invalid Option. Use 'b64tohex' or 'hextob64'.")


if __name__ == "__main__":
    main()