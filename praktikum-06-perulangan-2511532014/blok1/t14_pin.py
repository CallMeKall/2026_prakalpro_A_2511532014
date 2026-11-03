correct_pin = "1234"
MAX_ATTEMPTS = 3
attemp = 1
pin = input("Enter PIN: ")

while pin != correct_pin and attemp < MAX_ATTEMPTS:
    print("Incorrect PIN.")
    attemp += 1
    pin = input("Enter PIN: ")

if pin == correct_pin:
    print("Access granted")
else:
    print("Account locked")