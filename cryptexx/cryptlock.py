import base64
from colorama import Fore
def encrypt(text: str, key: str) -> str:
    if key == "":
        print(f"{Fore.RED}[ERROR]{Fore.RESET} An error occurred: encryption key cannot be none.")
    if text == "":
        print(f"{Fore.RED}[ERROR]{Fore.RESET} An error occurred: text to encrypt cannot be none.")

    encrypted_bytes = bytearray()
    key_len = len(key)
    for i, char in enumerate(text):
        shift = ord(key[i % key_len])
        encrypted_bytes.append((ord(char) + shift) % 256)
    
    return base64.b64encode(encrypted_bytes).decode()

def decrypt(text: str, key: str) -> str:
    if key == "":
        print(f"{Fore.RED}[ERROR]{Fore.RESET} An error occurred: encryption key cannot be none.")
    if text == "":
        print(f"{Fore.RED}[ERROR]{Fore.RESET} An error occurred: text to decrypt cannot be none.")
    encrypted_bytes = base64.b64decode(text)
    decrypted = ""
    key_len = len(key)
    for i, byte in enumerate(encrypted_bytes):
        shift = ord(key[i % key_len])
        decrypted += chr((byte - shift) % 256)
    return decrypted