from Crypto.Hash import HMAC, SHA256

# We have received a message 'msg' together
# with its MAC 'mac'

secret = b'Swordfish'
h = HMAC.new(secret, digestmod=SHA256)
h.update(msg)
try:
  h.hexverify(mac)
  print("The message '%s' is authentic" % msg)
except ValueError:
  print("The message or the key is wrong")