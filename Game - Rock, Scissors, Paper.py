import random

user_ball = 0
bot_ball = 0
draw = 0

while True:
    user = input("Input your choice (Rock,Scissors,Paper) : ")
    list_choice = ['Rock','Scissors','Paper']
    list_choice_bot = ['Rock','Scissors','Paper']
    if user in list_choice:
        bot = random.choice(list_choice_bot)
        print(bot)

        if bot == 'Rock' and user == 'Paper':
            user_ball += 1
            
        if bot == 'Paper' and user == 'Rock':
            bot_ball += 1
        
        if bot == 'Rock' and user == 'Scissors':
            bot_ball += 1

        if bot == 'Scissors' and user == 'Rock':
            user_ball += 1

        if bot == 'Scissors' and user == 'Paper':
            bot_ball += 1
            
        if bot == 'Paper' and user == 'Scissors':
            user_ball += 1
            
        if bot == 'Paper' and user == 'Paper':
            draw += 1   

        if bot == 'Rock' and user == 'Rock':
            draw += 1    

        if bot == 'Scissors' and user == 'Scissors':
            draw += 1

    elif user == 'B':
        print('Your : {}\nBot : {}\nDraw : {}'.format(user_ball, bot_ball, draw))
            