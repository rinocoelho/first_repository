from random import randint

menu_prompt = (
    '- Press A to START RACE\n'
    '- Press B to CHECK FUNDS\n'
    '- Press C for RACE HISTORY\n'
    '- Press D to RESET WALLET\n'
    '- Press Q to QUIT\n'
    '- Choose: '
)



# while loop na funcao MENU()!!!!!!!!!!!!

horses = [
    {'horse': 1, 'name': 'Ludovico', 'pay rate': 1.15, 'odds': .3},
    {'horse': 2, 'name': 'Greg', 'pay rate': 1.50, 'odds': .2},
    {'horse': 3, 'name': 'Jorge', 'pay rate': 2.00, 'odds': .18},
    {'horse': 4, 'name': 'Robinson', 'pay rate': 3.00, 'odds': .15},
    {'horse': 5, 'name': 'Nino', 'pay rate': 5.00, 'odds': .10},
    {'horse': 6, 'name': 'Carimbo', 'pay rate': 10.00, 'odds': .07}
]


def menu():
    user_input = ""
    wallet = 1000
    race = 0
    race_won = 0
    while user_input.upper() != 'Q':
        if wallet < 15:
            print("Insufficient funds")
            another_chance = input("Would you like to RESET YOUR WALLET? Y/N ")
            if another_chance == "Y":
                wallet = reset_wallet()
            elif another_chance == "N":
                print("BYE BYE")
                return
        if user_input.upper() == 'A':
            wallet, race, race_won = start_race(wallet, race, race_won)
        elif user_input.upper() == 'B':
            check_funds(wallet)
        elif user_input.upper() == 'C':
            race_history(race, race_won)
        elif user_input.upper() == 'D':
            wallet = reset_wallet()
        elif user_input == "":
            pass
        else:
            print('Unknown command. Please try again')
        user_input = input(menu_prompt)


def start_race(wallet, race, race_won):
    for horse in horses:
        list_of_horses = f'{horse["horse"]} {horse["name"]} / Pay rate: {horse["pay rate"]}'
        print(list_of_horses)
    for horse in horses:
        pick_int = 0
        while pick_int > 6 or pick_int < 1:
            try:
                print("Choose a number from 1 to 6")
                pick = input('Choose a horse: ')
                pick_int = int(pick)
            except ValueError:
                print ("Only Integers")
                continue
        race_result = randint(1, 100)
        bet_money_int = 0
        while bet_money_int < 10 or bet_money_int > 500:
            bet_money = input('Insert money for race: ')
            bet_money_int = int(bet_money)
        wallet = wallet - bet_money_int
        race += 1
        if pick == '1' and race_result <= 30:
            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)

            print(race_result)
            print(f"You won ${profit}")
            print(f'Your current funds are ${wallet}')

        elif pick == '2' and race_result > 30 and race_result <= 50:

            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)

            print(race_result)
            print(f"You won ${profit}")
            print(f'Your current funds are ${wallet}')

        elif pick == '3' and race_result > 50 and race_result <= 68:
            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)

            print(race_result)
            print(f"You won ${profit}")
            print(f'Your current funds are ${wallet}')

        elif pick == '4' and race_result > 68 and race_result <= 83:

            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)

            print(race_result)
            print(f"You won ${profit}")
            print(f'Your current funds are ${wallet}')

        elif pick == '5' and race_result > 83 and race_result <= 93:

            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)

            print(race_result)
            print(f"You won ${profit}")
            print(f'Your current funds are ${wallet}')

        elif pick == '6' and race_result > 93:
            race_won += 1

            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)
            print(race_result)
            print(f"You won ${profit}")
            print(f'Your current funds are ${wallet}')

        else:
            print("YOU LOST")

            print(f"Your current amount is {wallet}")

        return wallet, race, race_won



def check_funds(wallet):
    print (f'Your current funds are ${wallet}')
    return wallet

def race_history(race, race_won):
    print(f'Total : {race} races')
    print(f'Wins: {race_won} races')


def reset_wallet():
    wallet = 1000
    print('Your wallet has been reset')
    return wallet

#def maminha() #parametros da funcao bet_money_int, horse, wallet, race_won e retornar wallet & race_won

def picks(pick, race_result, bet_money_int, wallet, race_won, horse, race):
    if pick == '1' and race_result <= 30:
        race_won += 1
        pay_rate = horse["pay rate"]
        profit = round((bet_money_int * pay_rate) - bet_money_int)
        wallet += profit

        print(race_result)
        print(f"You won ${profit}")
        print(f'Your current funds are ${wallet}')

    elif pick == '2' and race_result > 30 and race_result <= 50:

        race_won += 1
        pay_rate = horse["pay rate"]
        profit = round((bet_money_int * pay_rate) - bet_money_int)
        wallet += profit

        print(race_result)
        print(f"You won ${profit}")
        print(f'Your current funds are ${wallet}')

    elif pick == '3' and race_result > 50 and race_result <= 68:
        race_won += 1
        pay_rate = horse["pay rate"]
        profit = round((bet_money_int * pay_rate) - bet_money_int)
        wallet += profit

        print(race_result)
        print(f"You won ${profit}")
        print(f'Your current funds are ${wallet}')

    elif pick == '4' and race_result > 68 and race_result <= 83:

        race_won += 1
        pay_rate = horse["pay rate"]
        profit = round((bet_money_int * pay_rate) - bet_money_int)
        wallet += profit

        print(race_result)
        print(f"You won ${profit}")
        print(f'Your current funds are ${wallet}')

    elif pick == '5' and race_result > 83 and race_result <= 93:

        race_won += 1
        pay_rate = horse["pay rate"]
        profit = round((bet_money_int * pay_rate) - bet_money_int)
        wallet += profit

        print(race_result)
        print(f"You won ${profit}")
        print(f'Your current funds are ${wallet}')

    elif pick == '6' and race_result > 93:
        race_won += 1

        pay_rate = horse["pay rate"]
        profit = round((bet_money_int * pay_rate) - bet_money_int)
        wallet += profit
        print(race_result)
        print(f"You won ${profit}")
        print(f'Your current funds are ${wallet}')

    else:
        print("YOU LOST")

        print(f"Your current amount is {wallet}")

    return wallet, race, race_won



menu()

# print(display)
# amount_to_spend = input('How much $ do you want to spend? (NUMBERS ONLY) ')
# winner = f'{name} has won the race'
# bet_money = (amount_to_spend * int(rate))
# wallet_message = f'You won {bet_money}'

