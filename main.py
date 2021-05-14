import random
from game_data import  data
from art import logo, vs
from replit import clear


def random_choice() :
   return random.choice(data)

def format_choice(account) :
  name=account['name']
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"


def check_answer(guess,a_follower,b_follower) :
  if a_follower > b_follower :
    return guess=="a"
  else :
    return guess=="b" 


def game() :
  print(logo)
  score= 0
  game_should_continue = True
  account_a = random_choice()
  account_b = random_choice()
  
  
  while game_should_continue :
    account_a = account_b
    account_b= random_choice()
    
    while account_a==account_b :
      account_b=random_choice()

    print(f"Compare A :{format_choice(account_a)}")
    print(vs)
    print(f"Compare B :{format_choice(account_b)}")

    guess=input("Which is correct 'A' or 'B' :").lower()
    a_follower_count=account_a['follower_count']
    b_follower_count=account_b['follower_count']
    is_correct=check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct :
      score+=1
      print(f"You are right .Your Score is {score}")
    else :
      game_should_continue=False
      print(f"You are wrong. You lost. Your final score is {score}")
    
game()
play_again=input("Do you want to play again type 'y to play again' and 'n' if you don't want to").lower()
if play_again=="y" :
  clear()
  game()
else : 
  print("Nice meeting you")

  
