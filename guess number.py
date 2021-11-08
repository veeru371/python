import random
system_guess=random.randint(1,88)
user_guess=int(input('guess the number'))
print(f'user_guess-{user_guess} and system_guess-{system_guess}')
if(user_guess==system_guess):
     print('your guess is correct')
else:
         print('your guess is not correct')
