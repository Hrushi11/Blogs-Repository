from RPS_Bot import *
rps_labels = [ "rock", "paper", "scissor"]

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