from Crypto.Hash import KMAC128

# We have received a message 'msg' together
# with its MAC 'mac'

secret = b'Sixteen byte key'
mac = KMAC128.new(key=secret, mac_len=16)
mac.update(msg)
try:
  mac.verify(mac)
  print("The message '%s' is authentic" % msg)
except ValueError:
  print("The message or the key is wrong")