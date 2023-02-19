from sympy import mod_inverse
class Cipher:
    def __init__(self,a:int,b:int):
        self.a = a
        self.b = b
        self.ciphertext = ""
        self.plaintext = ""
        
    def Encrypt(self):
        #take input from the user to encrypt
        self.plaintext = input("what is the plaintext : ")
        
        for x in range(len(self.plaintext)): 
            offset=65
            if self.plaintext[x].islower(): offset=97
            
            self.ciphertext+=chr(((ord(self.plaintext[x])*self.a+self.b-offset)%26)+offset)
        return self.ciphertext
    def Decrypt(self):
        #D(X)=(Y-b)*a^-1 mod 26
        self.ciphertext=input("what is the ciphertext : ")
        inverse=mod_inverse(self.a,26)
        for x in range(len(self.ciphertext)):
            offset=65
            if self.ciphertext[x].islower(): offset=97
            self.plaintext+=chr(((ord(self.ciphertext[x])-self.b)*inverse-offset)%26 +offset)
        return self.plaintext.replace("T"," ")    

    def __str__(self):
        return "the plaintext is : "+self.plaintext +" \nthe key a is : "+str(self.a) +" \nthe key b :"+str(self.b) 
