print('Welcome participants to my quiz!!')
participants = input('Are you interested in participating in this quiz? ')
if participants.lower() != 'yes':
    quit()
print('Let the quiz begin!!')
score = 0
answer = input('How many countries are there in Africa?')
if answer == '54':
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
answer = input(' What year did the United States gain its independence?')
if answer == '1776':
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
answer = input('How many continents are there in the world?')
if answer == '7':
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
answer = input('How many letters are there in the alphabet?')
if answer == '26':
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
answer = input('Who was the first black president of the United States')
if answer.lower() == 'barrack obama':
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
print('Your total score is ' + str(score) + ' out of 5')
print('You got ' + str((score/4)* 100) + '%')
