from Cipher import Cipher 

print("\twelcom to the Affine cipher \t")
print("what is the key of the affine cipher (a,b)")
a=int(input("what is a: "))
b=int(input("what is b: "))
print("Do you want to encrypt or decrypt ")
choice=int(input("choose 1.to encrypt or 2. to decrypt "))
obj=Cipher(a,b)

if choice==1: print("the Encrypted value is : "+ obj.Encrypt())
elif choice==2: print("the Decrypted value is : "+ obj.Decrypt())
else: obj.__str__()





