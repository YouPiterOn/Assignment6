import assignment5
import assignment6
b = input("Choose assignment: ")

if b == '5':
    assignment5.caesar_cipher()
elif b == '6':
    text = input("Enter text: ")
    crypted = assignment5.secret_mode(text)
    a = assignment6.automatic_cracking(crypted)
    print(a)
