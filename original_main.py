import sys
from converter_base64 import base64_tohex, hex_to_base64

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

