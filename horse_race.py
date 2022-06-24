from random import randint

menu_prompt = (
    '- Press A to START RACE\n'
    '- Press B to CHECK FUNDS\n'
    '- Press C for RACE HISTORY\n'
    '- Press D to RESET WALLET\n'
    '- Press X to BACK UP WALLET\n'
    '- Press Z for TOP FIVE BETS\n'
    '- Press Q to QUIT\n'
    '- Choose: '
)


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
    reset = 0
    profit_list = [0,0,0,0,0]
    while user_input.upper() != 'Q':
        if wallet < 10:
            print("Insufficient funds")
            another_chance = input("Would you like to RESET YOUR WALLET? Y/N ")
            if another_chance == "Y":
                wallet = reset_wallet(reset)
            elif another_chance == "N":
                print("BYE BYE")
                return
        if user_input.upper() == 'A':
            wallet, race, race_won, profit_list = start_race(wallet, race, race_won, profit_list)
        elif user_input.upper() == 'B':
            check_funds(wallet)
        elif user_input.upper() == 'C':
            race_history(race, race_won)
        elif user_input.upper() == 'D':
            wallet = reset_wallet(reset)
            reset += 1
            if reset > 3:
                print("You've reached the limit of resets")
                return
        elif user_input == "":
            pass
        elif user_input.upper() == "X":
            wallet = backup_wallet(wallet)
        elif user_input.upper() == "Z":
            show_top_five()
        else:
            print('Unknown command. Please try again')
        user_input = input(menu_prompt)
    save_wallet(wallet)


def start_race(wallet, race, race_won, profit_list):
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
            try:
                bet_money = input('Insert money for race: ')
                bet_money_int = int(bet_money)
            except ValueError:
                print("Only Integers")
                continue
        wallet = wallet - bet_money_int
        race += 1
        if pick == '1' and race_result <= 30:
            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)
            profit_list.append(profit)
            print(race_result)
            print(f"YOU WON ${profit}")
            print(f'Your current funds are ${wallet}')
            top_five(profit_list)


        elif pick == '2' and race_result > 30 and race_result <= 50:

            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)
            profit_list.append(profit)
            print(race_result)
            print(f"YOU WON ${profit}")
            print(f'Your current funds are ${wallet}')
            top_five(profit_list)



        elif pick == '3' and race_result > 50 and race_result <= 68:
            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)
            profit_list.append(profit)
            print(race_result)
            print(f"YOU WON ${profit}")
            print(f'Your current funds are ${wallet}')
            top_five(profit_list)



        elif pick == '4' and race_result > 68 and race_result <= 83:

            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)
            profit_list.append(profit)
            print(race_result)
            print(f"YOU WON ${profit}")
            print(f'Your current funds are ${wallet}')
            top_five(profit_list)



        elif pick == '5' and race_result > 83 and race_result <= 93:

            race_won += 1
            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)
            profit_list.append(profit)
            print(race_result)
            print(f"YOU WON ${profit}")
            print(f'Your current funds are ${wallet}')
            top_five(profit_list)



        elif pick == '6' and race_result > 93:
            race_won += 1

            pay_rate = horse["pay rate"]
            profit = round((bet_money_int * pay_rate) - bet_money_int)
            wallet += (profit + bet_money_int)
            profit_list.append(profit)
            print(race_result)
            print(f"YOU WON ${profit}")
            print(f'Your current funds are ${wallet}')
            top_five(profit_list)


        else:
            print("YOU LOST")

            print(f"Your current funds are ${wallet}")



        return wallet, race, race_won, profit_list



def check_funds(wallet):
    print (f'Your current funds are ${wallet}')
    return wallet

def race_history(race, race_won):
    print(f'Total : {race} races')
    print(f'Wins: {race_won} races')


def reset_wallet(reset):
    while reset < 3:
        wallet = 1000
        print('Your wallet has been reset')
        return wallet

def save_wallet(wallet):
    save = open("backup_wallet.txt", "w")
    wallet_string = str(wallet)
    save.write(wallet_string)
    save.close()

def backup_wallet(wallet):
    backup =  open("backup_wallet.txt", "r")
    read_backup =  backup.readline()
    int_read_backup = int(read_backup)
    wallet = int_read_backup
    print(wallet)
    return wallet

def top_five(profit_list):
    n = len(profit_list)
    count = 0
    for l in range(n-1):
        top = open("top_five.txt", "w")
        for x in range(n-1):
            if profit_list[x] < profit_list[x + 1]:
        #troca de elementos nas posicoes x e x+1
                profit_list[x], profit_list[x+1] = profit_list[x+1], profit_list[x]

        for bet in profit_list[:5]:
            count +=1
            top.write(f"{bet} IS RANKED {count} \n\n")
            #print(profit_list[:5])

        if count > 4 and profit_list[:5]:
            count = 0

    #save_top = open("top_five.txt", "r")
    #read_top = save_top.readlines()
    #profit_list = read_top
    #print(profit_list)
    #return profit_list
        #str_profit = str(profit_list[-5:])
        #top.write(f"{str_profit}\n")
    #top.close()

def show_top_five():
    show = open("top_five.txt", "r")
    look_up = [line.strip() for line in show.readlines()]
    for line in look_up:
        print(f"\n {line}")
    show.close()



menu()



# print(display)
# amount_to_spend = input('How much $ do you want to spend? (NUMBERS ONLY) ')
# winner = f'{name} has won the race'
# bet_money = (amount_to_spend * int(rate))
# wallet_message = f'You won {bet_money}'

