import random
num = input('Enter a number: ')
if num.isdigit():
    num = int(num)
    if num<= 0:
        print('Type a larger number')
        quit()
else:
    print('Enter a number!!')
    quit() 
r = random.randint(0,  num)
attempts = 0
while True:
    attempts +=1
    guess = int(input('Guess a number between o and your first number'))
    if guess == r:
        print('You got it!!')
        break
    elif guess > r:
            print('Your number is greater than the correct number.')
    else:
            print('Your number is less than the correct number.')

print(f'You got it in {attempts} tries')
