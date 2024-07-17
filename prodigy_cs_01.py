def caesar_cipher(shift, message, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for letter in message:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (E/D): ").strip().upper()
        if choice in {"E", "D"}:
            message = input("Enter the message: ").strip()
            shift = int(input("Enter the shift value: ").strip())
            if choice == "E":
                print("Encrypted message:", caesar_cipher(shift, message, encrypt=True))
            else:
                print("Decrypted message:", caesar_cipher(shift, message, encrypt=False))
        else:
            print("Invalid choice. Please try again.")
        
        cont = input("Do you want to continue? (Y/N): ").strip().upper()
        if cont != "Y":
            break

if __name__ == "__main__":
    main()
