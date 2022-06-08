#GUESSING GAME WITHOUT LOOPING.
import random
computer=random.randint(1,10)
#print(computer)
player=int(input('Guess the number between (1:10) : '))
set1=player < computer
set2= player > computer
if   set1  :
    print('You are so close ! ')
elif set2   :
    print('You are a bit far from it ! ')
elif player == computer :
    print('You guessed right !\nLucky you !')   
else:
    print('Try again')
print(f"The computer played '{computer}'")
            