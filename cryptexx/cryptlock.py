import base64

def encrypt(text: str, key: str) -> str:
    encrypted_bytes = bytearray()
    key_len = len(key)
    for i, char in enumerate(text):
        shift = ord(key[i % key_len])
        encrypted_bytes.append((ord(char) + shift) % 256)
    
    return base64.b64encode(encrypted_bytes).decode()

def decrypt(ciphertext: str, key: str) -> str:
    encrypted_bytes = base64.b64decode(ciphertext)
    decrypted = ""
    key_len = len(key)
    for i, byte in enumerate(encrypted_bytes):
        shift = ord(key[i % key_len])
        decrypted += chr((byte - shift) % 256)
    return decrypted