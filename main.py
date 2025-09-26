import sys
from converter_base64 import base64_tohex, hex_to_base64


def main():
    try: 
        if len(sys.argv) < 3:
            print("\n How to use: python3 file.py 1 'Zg=='")
            print("1 - Base64 to Hex, 2 - Hex to Base64\n")
            return 
        
        choice = sys.argv[1]
        cstring = sys.argv[2]

        if choice == '1':
            hex_result = base64_tohex(cstring)
            print(f"Hex result: {hex_result}")
        elif choice == '2':
            base64_result = hex_to_base64(cstring)
            print(f"Base64 result: {base64_result}")
        else:
            print("Invalid choice. Please enter 1 or 2.")      
    except Exception as e:
        print(f"Erro on the main flow {e}")

if __name__ == "__main__":
    main()

