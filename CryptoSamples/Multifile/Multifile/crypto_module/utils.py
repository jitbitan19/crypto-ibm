from Crypto.Random import get_random_bytes
def generate_key():
    return get_random_bytes(16)  # AES-128 bit key
def read_key_from_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()
def write_key_to_file(key, filepath):
    with open(filepath, 'wb') as f:
        f.write(key)