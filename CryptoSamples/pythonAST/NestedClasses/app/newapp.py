from crypto.aes import MyCrypto


class app:
    def __init__ (self):
        print("I am initialised")           
    def encrypt(self):
        crypto = MyCrypto
        crypto.generateKey()
        crypto.generateIV()
        encyptedText = crypto.encrypt()
        print(encyptedText)

# Defining main function 
def main(): 
    myapp = app.encrypt()
    print(myapp)
  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 