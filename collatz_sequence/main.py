# The Collatz sequence is a mathematical sequence where you start with a positive integer. If it's even,
# you divide it by 2; if it's odd, you multiply it by 3 and add 1. Repeat this process with the resulting number.
# The conjecture is that, regardless of the starting value, the sequence will always eventually reach 1.

def collatz(number):
    if number % 2 == 0:
        new_number = number // 2
        print(new_number)
    else:
        new_number = 3 * number + 1
        print(new_number)
    return new_number


user_input = input('Choose a number: ')
selected_number = int(user_input)

while selected_number != 1:
    selected_number = collatz(selected_number)