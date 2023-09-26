from random import choice

SIGNS = ["rock", "papper", "scissors"]

def main():
    print(f"welcome to the { ','.join (SIGNS)} game!")
    print_rules()
    game_loop(3)


def print_rules():
    print("\neach player picks only 1 sign")
    for winners, losers in zip([0,1,2],[2,0,1]):
      print(f"{SIGNS[winners].title()} wins over {SIGNS[losers]}")

def game_loop(number_of_rounds):
    for current_round in range(1,number_of_rounds + 1):
        print(f"round{current_round}")

        sign_player_a = get_sign_from_user()
        sign_player_b = get_sign_from_computer()
        print(f"player: {sign_player_a}, computer: {sign_player_b}")

        if is_draw(sign_player_a, sign_player_b):
            print("its a draw!")
        elif wins_over(sign_player_a, sign_player_b):
            print("player wins!")
        else:
            print("the computer wins :( ")

    


def get_sign_from_user():
    while True:
     sign = input("pick a sign out of the 3")
    
     if sign in SIGNS: 
         return sign
    else:
        print(f"you must pick any of the following {','.join(SIGNS)}")

def get_sign_from_computer():
    return choice(SIGNS)



def is_draw(sign_a, sign_b):
    return sign_a == sign_b


def wins_over(sign_a, sign_b):
    ...
main()