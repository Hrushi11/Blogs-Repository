import random

class User:
    def __init__(self, name, age, email):
        self.age = age
        self.name = name
        self.email = email
    
    def sign_in(self):
        sgn_in = "LOGGED IN" if int(self.age) >= 3 else f"UDER-AGE, LOGGED OUT - {self.age} years"
        
        return sgn_in
    
    def profile(self):
        prf = f"Name - {self.name} \nAge - {self.age} \nEmail - {self.email}."
        
        return prf
    
rps_labels = [ "rock", "paper", "scissor"]

class RPS_Bot(User):
     def __init__(self, name, age, email, choice):
        self.age = age
        self.name = name
        self.email = email
        self.choice = choice
        self.bot_choice = "BOT CHOICE NOT INIITIALIZED YET"
    
     def rps_bot(self):
         c = 1
         players = [self.name, "RPS-BOT"]
         user_choice = self.choice.lower()
         bot_choice = random.choice(rps_labels)
         orig = [user_choice, bot_choice]
         check = [user_choice, bot_choice]
         check.sort()
         
         if check[0] == check[1]:
             c = 0
             res = "DRAW"
         
         if check == ['paper', 'rock']:
             res = "paper"
         elif check == ["paper", "scissor"]:
             res = "scissor"
         elif check == ["rock", "scissor"]:
             res = "rock"
         
         if c:
             for i in range(len(orig)):
                 if res == orig[i]:
                     index = i
             res = f"{players[index]} won"     
         
         return res, user_choice, bot_choice
        
     def rps_initiate(self):
         print("-------------------------------------------")
         if int(self.age) >= 3:
             res, user_choice, bot_choice = self.rps_bot()
             stmnt = f"{res} \n{self.name} Chose - {user_choice} \nRPS-BOT Chose - {bot_choice}"
         
         else :
             stmnt = f"YOU ARE UNDER-AGE - {self.age} years \nCHECK with `sign_in()` function"

         return stmnt


def run():
    name = input("Enter your name \n")
    age = input("Enter your age \n")
    email = input("Enter your email \n")
    choice = input("Choose from `ROCK`, `PAPER`, `SCISSOR` \n")
    
    return name, age, email, choice

name, age, email, choice  = run()

if choice.lower() in rps_labels:
    bot1 = RPS_Bot(name, age, 
                   email, 
                   choice)
    print(bot1.rps_initiate())
    print("-------------------------------------------")
else:
    print(f"YOU chose `{choice}`, which is not identified, RE-CHECK")