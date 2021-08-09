from RPS_Bot import *

def run():
    name = input("Enter your name \n")
    age = input("Enter your age \n")
    email = input("Enter your email \n")
    choice = input("Choose from `ROCK`, `PAPER`, `SCISSOR` \n")
    
    return name, age, email, choice

name, age, email, choice  = run()

bot1 = RPS_Bot(name, age, 
               email, 
               choice)
print(bot1.rps_initiate())
print("-------------------------------------------")
