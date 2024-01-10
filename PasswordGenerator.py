# Passowrd Generator
import random

interests = []
symbols = ['!','#','@', '&']



with open('interests.txt') as interests_doc:
    interests = interests_doc.readlines()
    for i in range(len(interests)-1):
        interests[i] = interests[i][:-1]        

def generate_password(length):
    rand_interest = random.choice(interests)
    rand_symbol = random.choice(symbols)
    password_length = len(rand_interest) + 1
    if password_length > int(length): digit_len = 2
    else: digit_len = pow(10,(int(length) - password_length))
    print(digit_len)
    random_numbers = random.randint(digit_len,digit_len*9)
    new_password = f"{rand_interest}{rand_symbol}{random_numbers}"
    return new_password

is_running = True

# Mobile Friendly
print('Random Generated Passwords')
while is_running:
    print('---------------------------')
    length = input("Enter Password Length: ")
    print(generate_password(length))
    user_input = input('Press Enter to Generate 3 more, type "q" to quit: ')
    if not user_input == '':
        quit(0)


