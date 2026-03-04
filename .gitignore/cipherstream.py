import random

class StreamCipher:
    def __init__(self, key):
        self.key = key
        self.prng_state = self.seed_prng(key)

    def seed_prng(self, key):
        # Seed the PRNG using the key
        seed = sum(ord(char) for char in key)
        random.seed(seed)
        return seed

    def generate_keystream(self, length):
        # Generate a keystream of the given length
        keystream = []
        for _ in range(length):
            keystream.append(random.randint(0, 255))  # Generate a random byte (0-255)
        return keystream

    def encrypt(self, plaintext):
        # Convert plaintext to bytes
        plaintext_bytes = [ord(char) for char in plaintext]
        keystream = self.generate_keystream(len(plaintext_bytes))
        
        # XOR each byte of plaintext with the keystream
        ciphertext = [plaintext_bytes[i] ^ keystream[i] for i in range(len(plaintext_bytes))]
        return ciphertext

    def decrypt(self, ciphertext):
        # Generate the same keystream for decryption
        keystream = self.generate_keystream(len(ciphertext))
        
        # XOR each byte of ciphertext with the keystream
        plaintext_bytes = [ciphertext[i] ^ keystream[i] for i in range(len(ciphertext))]
        plaintext = ''.join(chr(byte) for byte in plaintext_bytes)
        return plaintext

# Example usage
key = "mysecretkey"
cipher = StreamCipher(key)

plaintext = "Hello Internet, Welcome to world of our infinite possibilities"
print("Plaintext:", plaintext)

ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted Text:", decrypted_text)