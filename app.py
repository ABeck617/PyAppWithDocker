print("Hello, World!") 

# app.py
with open('secret.txt', 'r') as file:
    secret = file.read().strip()
print(f"Hello, World! The secret is: {secret}")

