from Crypto.Hash import Poly1305
from Crypto.Cipher import AES
from binascii import unhexlify

# We have received a message 'msg' together
# with its MAC 'mac_tag_hex' and the nonce 'nonce_hex'

secret = b'Thirtytwo very very secret bytes'
nonce = unhexlify(nonce_hex)
mac = Poly1305.new(key=secret, nonce=nonce, cipher=AES, data=msg)
try:
  mac.hexverify(mac_tag_hex)
  print("The message '%s' is authentic" % msg)
except ValueError:
  print("The message or the key is wrong")