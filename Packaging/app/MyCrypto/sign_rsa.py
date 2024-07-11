from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA3_256
from Crypto.PublicKey import RSA


def gen_rsa_sign_key(key_size: int, key_name: str):
    """
    A key pair geneator for RSA signing
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


def rsa_sign(msg: str, key_name: str) -> str:
    """
    An RSA signer
    # Parameters:
        `msg`: message to be signed
        `key_name`: reference to the private key ({key_name}__rsa_pvt_key.pem)
    # Returns:
        Hex of the signature
    """
    try:
        with open(f"{key_name}__rsa_pvt_key.pem", "rb") as f:
            key = RSA.import_key(f.read())
        signer = PKCS1_v1_5.new(key)
        return signer.sign(SHA3_256.new(msg.encode())).hex()
    except:
        print(f"Key not found")
        return " "


def rsa_verify(msg: str, sign: str, key_name: str) -> bool:
    """
    An RSA validator
    # Parameters:
        `msg`: signed message
        `sign`: signature (in hex)
        `key_name`: reference to the public key ({key_name}__rsa_pub_key.pem)
    """
    with open(f"{key_name}__rsa_pub_key.pem", "rb") as f:
        key = RSA.import_key(f.read())
    validator = PKCS1_v1_5.new(key)
    return validator.verify(SHA3_256.new(msg.encode()), bytes.fromhex(sign))
