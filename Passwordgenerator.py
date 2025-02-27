import random
import string

password = input("Do you want to generate a password? (Y/N): ").strip().lower()

if password == 'y':
    lenofpassword = int(input("What should be the length of the password? "))
    print("Length:", lenofpassword)
    
    # Generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(lenofpassword))
    
    print("Generated Password:", generated_password)
else:
    print("Okay! No password generated.")
