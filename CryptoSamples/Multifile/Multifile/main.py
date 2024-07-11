from crypto_module.aes_cipher import AESCipher
from crypto_module.utils import generate_key, write_key_to_file, read_key_from_file
def main():
    # Generate and save the key
    #key = generate_key()
    #key_file = 'aes_key.bin'
    #write_key_to_file(key, key_file)
    # Read the key from file
    #key = read_key_from_file(key_file)
    # Create an instance of AESCipher
    aes_cipher = AESCipher()
    # Encrypt data
    data = "This is a secret message"
    iv, ct = aes_cipher.encrypt(data)
    print(f"Encrypted: IV={iv}, CipherText={ct}")
    # Decrypt data
    #decrypted_data = aes_cipher.decrypt(iv, ct)
    #print(f"Decrypted: {decrypted_data}")
if __name__ == "__main__":
    main()