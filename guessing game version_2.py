#GUESSING GAME WITH LOOPING.
import random
computer=random.randint(1,10)
player=None
user=None
while True:
     computer=random.randint(1,10)
     player=int(input('Guess a number between (1:10) : '))
     print(f"The computer played '{computer}' ")
     set1=player < computer
     set2= player > computer
     if  set1  :
         print('You are so close ! ')
     elif  set2   :
         print('You are a bit far from it ! ')
     elif  player == computer :
         print('You guessed right ! \nLucky you !')     
     else:
         print('Try again ! ')
        
     user=input('do you want to continue (y/n)  ').lower()
     if user == 'n' :
          break
     elif user == 'y' :
         computer=random.randint(1,10)
    
