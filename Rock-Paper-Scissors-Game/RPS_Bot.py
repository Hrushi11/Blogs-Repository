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
         c = 1 # Check for winning
         players = [self.name, "RPS-BOT"]
         user_choice = self.choice.lower() # to keep similarities all throughout
         bot_choice = random.choice(rps_labels)
         self.bot_choice = bot_choice
         orig = [user_choice, bot_choice] # original order
         check = [user_choice, bot_choice] # order will be changed after sorting
         check.sort() # to sort the array
         
         if check[0] == check[1]: 
             c = 0
             res = "DRAW"
         
         if check == ['paper', 'rock']: 
             res = "paper"
         elif check == ["paper", "scissor"]:
             res = "scissor"
         elif check == ["rock", "scissor"]:
             res = "rock"
         
         if c: # works if it's not a draw
             for i in range(len(orig)): 
                 if res == orig[i]: 
                     index = i # to get the position of the winner from the orig array
             res = f"{players[index]} won"     
         
         return res, user_choice, bot_choice # returning results, user choice and bot choice
        
     def rps_initiate(self):
         print("-------------------------------------------")
         if int(self.age) >= 3 and self.choice.lower() in rps_labels:
             res, user_choice, bot_choice = self.rps_bot()
             stmnt = f"{res} \n{self.name} Chose - {user_choice} \nRPS-BOT Chose - {bot_choice}"
         
         else :
             stmnt = f"YOU MIGHT BE UNDER-AGE - {self.age} years, or \nyou chose `{self.choice}`, which might NOT BE IDENTIFIED, RE-CHECK "

         return stmnt
