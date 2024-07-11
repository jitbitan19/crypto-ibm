from Crypto.Hash import CMAC
from Crypto.Cipher import AES

# We have received a message 'msg' together
# with its MAC 'mac'

secret = b'Sixteen byte key'
cobj = CMAC.new(secret, ciphermod=AES)
cobj.update(msg)
try:
  cobj.verify(mac)
  print("The message '%s' is authentic" % msg)
except ValueError:
  print("The message or the key is wrong")