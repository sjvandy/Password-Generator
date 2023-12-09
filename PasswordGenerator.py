# Passowrd Generator
import random

interests = []
symbols = ['.','#','-']



with open('interests.txt') as interests_doc:
    interests = interests_doc.readlines()
    for i in range(len(interests)-1):
        interests[i] = interests[i][:-1]        

def generate_passwords():
    # Generate Random Items
    rand_interest = random.choice(interests)
    rand_symbol = random.choice(symbols)
    two_digit = random.randint(10,99)
    four_digit = random.randint(1000,9999)
    six_digit = random.randint(100000, 999999)
    # Create 3 Unique Passwords
    two_digit_password = f"{rand_interest}{rand_symbol}{two_digit}"
    four_digit_password = f"{rand_interest}{rand_symbol}{four_digit}"
    six_digit_password = f"{rand_interest}{rand_symbol}{six_digit}"

    return two_digit_password, four_digit_password, six_digit_password

is_running = True

# Mobile Friendly
print('Random Generated Passwords')
while is_running:
    print('---------------------------')
    pass1, pass2, pass3 = generate_passwords()
    print(pass1)
    print(pass2)
    print(pass3)
    user_input = input('Press Enter to Generate 3 more, type "q" to quit: ')
    if not user_input == '':
        is_running = False


