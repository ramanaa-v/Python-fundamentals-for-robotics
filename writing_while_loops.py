# Basic while loops
count = 0
while count < 5:
    print('Count:', count)
    count += 1

# While loop with user input
user_input = ""
while user_input.lower() != 'quit':
    user_input = input("Enter 'quit' to exit: ")
    print('You entered', user_input)

# Using break statement in a while loop
count = 0
while True:
    if count == 5:
        break
    print("Looping:", count)
    count += 1

print("")
