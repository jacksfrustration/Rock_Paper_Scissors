import random as rand

moves=["Rock","Paper","Scissors"]
ascii_moves=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
             """
                  _______
             ---'    ____)____
                        ______)
                       _______)
                      _______)
             ---.__________)
             """,
             """
                 _______
             ---'   ____)____
                       ______)
                    __________)
                   (____)
             ---.__(___)
             """
             ]
user_score=0
computer_score=0
while True:
    start_playing=input("Start playing?\n").lower()
    if start_playing=="y" or start_playing=="ye" or start_playing== "yes":
        game_is_on=True
    else:
        game_is_on=False
    while game_is_on:
        user_move=input("What is your move?\n").title()
        computer_move_index=rand.randint(0, 2)
        computer_move=moves[computer_move_index].title()

        user_move_index=moves.index(user_move)
        print(f"Your move:{moves[user_move_index]}\n"
              f"{ascii_moves[user_move_index]}\n"
              f"Computer Move: {moves[computer_move_index]}\n"
              f"{ascii_moves[computer_move_index]}")
        if user_move.title()=="Paper" and computer_move=="Rock" or user_move=="Scissors" and computer_move=="paper" or user_move=="Rock" and computer_move=="Scissors":
            user_score+=1
            print(f"You win!! \nUser Score is: \t{user_score}\n"
                  f"\tComputer Score is: \t {computer_score}")
        elif user_move.title()==computer_move.title():
            print(f"The match was tied!! \nUser Score: {user_score}\n"
                  f"Computer score: {computer_score}")
        else:
            computer_score+=1
            print(f"You lose!! \nUser Score is: {user_score}\n"
                  f"Computer Score is: {computer_score}")