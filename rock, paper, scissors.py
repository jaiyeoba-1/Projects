import random
user_wins = 0
computer_wins = 0
items = ['rock','paper','scissors']
while True: 
    user_input = input('Type either rock, paper, scissors or Q to quit').lower()
    if user_input == 'q':
        break
    if user_input not in items:
        continue
    num = random.randint(0,2)
    # 0 = rock, 1 = paper, 2 = scissors
    computer_input = items[num]
    print('The computer picked', computer_input + '.')
    if user_input == computer_input:
        print('Draw') 
        
    if user_input == 'rock' and computer_input == 'scissors':
        print('You win!')
        user_wins +=1 
        
    elif user_input == 'paper' and computer_input == 'rock':
        print('You win!')
        user_wins +=1 
        
    elif user_input == 'scissors' and computer_input == 'paper':
        print('You win!')
        user_wins +=1 
        
    else: 
        print('The computer won!')
        computer_wins +=1
quit()
         
print('You won', user_wins ,'times.')
print('The computer won', computer_wins ,'times.')
