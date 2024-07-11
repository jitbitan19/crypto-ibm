
#import sys 
# adding Folder_2 to the system path
#sys.path.insert(0, "C:/WS-QS/quantum-safe-python/NestedClasses/crypto")
import crypto.aes as aes
class app:
    def __init__ (self):
        print("I am initialised")           
    def encrypt(self):
        crypto = aes.MyCrypto
        key=crypto.generateKey()
        iv=crypto.generateIV()
        encyptedText = crypto.encrypt(key,iv,'Test') # type: ignore
        print(encyptedText)

# Defining main function 
def main(): 
    myapp = app.encrypt() # type: ignore
    print(myapp)
  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 