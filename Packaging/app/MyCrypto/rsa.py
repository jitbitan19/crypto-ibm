from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def gen_rsa_key(key_size: int, key_name: str):
    """
    A key pair generator for RSA signing
    # Parameters:
        `key_size`: size of the key pair
        `key_name`: a name for referencing the key
    # Actions:
        Creates an RSA key pair (public key, private key)
    """
    key_pair = RSA.generate(key_size)
    pub_key = key_pair.public_key()
    with open(f"{key_name}__rsa_pub_key.pem", "wb") as f:
        data = pub_key.export_key()
        f.write(data)
    with open(f"{key_name}__rsa_pvt_key.pem", "wb") as f:
        data = key_pair.export_key()
        f.write(data)


def rsa_enc(msg: str, key_name: str) -> str:
    """
    An RSA encoder
    # Parameters:
        `msg`: message to be encoded
        `key_name`: reference to the public key, ({name}__rsa_pub_key.pem)
    # Returns:
        Hex of resulting cipher
    """
    try:
        with open(f"{key_name}__rsa_pub_key.pem", "rb") as f:
            data = f.read()
            key = RSA.import_key(data)
        rsa_cipher = PKCS1_OAEP.new(key=key)
        ct = rsa_cipher.encrypt(msg.encode())
        return ct.hex()
    except:
        print("Key pair not found")
        return " "


def rsa_dec(cipher: str, key_name: str) -> str:
    """
    An RSA decoder
    # Parameters:
        `cipher`: cipher text to be deciphered (in hex)
        `key_name`: reference to the private key, ({name}__rsa_pvt_key.pem)
    # Returns:
        Plain text of given cipher
    """
    with open(f"{key_name}__rsa_pvt_key.pem", "rb") as f:
        data = f.read()
        key = RSA.import_key(data)
    rsa_decipher = PKCS1_OAEP.new(key=key)
    try:
        pt = rsa_decipher.decrypt(bytes.fromhex(cipher))
        try:
            return pt.decode()
        except:
            return pt.hex()
    except:
        return " "
