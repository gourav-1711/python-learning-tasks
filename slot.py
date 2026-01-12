import random
slots = ('🍒',' 🍉','🍋','🥑', '⭐')

def jackpot(bet ,  symbol):
    multiply = 1
    match symbol:
        case "🍒":
            multiply = 2
        case "🍉":
            multiply = 3
        case "🍋":
            multiply = 4
        case "🥑":
            multiply = 5
        case "⭐":
            multiply = 10
    
    print(f"YOU WON : {bet * multiply}")
    return bet * multiply

def spin():
    
    slotNumber = random.randint(0,4)
    return slotNumber

def game():
    balance = 10000
    playing = True
    bet = 0
    spinnedSlots = ["","",""]
    print("********************************")
    print("WELCOME TO THE SLOT MACHINE")
    print(f"YOUR BALANCE IS : {balance:.2f}$")
    print( "symbols: 🍒 🍉 🍋🥑 ⭐ ")
    print("🍒 = *2 \n🍉= *3 \n🍋 = *4 \n🥑 = *5 \n⭐ = *10 \n")
    print("*********************************")

    while playing and balance > 0:
        print(f"PLACE YOUR BET")
        bet = input()
        if not bet.isdigit():
            print("ENTER A RIGHT AMOUNT")
            continue

        bet = float(bet)
        if bet < 0:
            print("ENTER AMOUNT BIGGER THAN 0")
            continue

        if bet > balance:
            print("INSUFFIECIENT BALANCE")
            continue



        balance -= bet

        print(f"SPINNIG THE MACHINE \n")
        # spinnedSlots[0] = slots[spin()]
        # spinnedSlots[1] = slots[spin()]
        # spinnedSlots[2] = slots[spin()]
        spinnedSlots = [random.choice(slots) for _ in range(3)]

        for slot in spinnedSlots:
            print(slot , end="\t")

        print()
        if spinnedSlots[0] == spinnedSlots[1] and spinnedSlots[1] == spinnedSlots[2]:
            print("\n********************************")
            print("YOU WON ! CONGRATULATIONS")
            balance += jackpot(bet , spinnedSlots[0]) + bet
            print(f"YOUR BALANCE NOW IS : {balance}")
            print("********************************")
        else:
            print("********************************")
            print("\nBETTER LUCK IN NEXT TRY ")
            print(f"YOUR BALANCE : {balance}")
            print("********************************")
            if playing and balance > 0:
                continue
            else:
                playing = False
                print("YOU RAN OUT OF MONEY START AGAIN : Y/N")
                choice = input().lower()
                if choice == "y":
                    balance = 10000
                    playing = True
                else:
                    playing = False

        # print(spinnedSlots)    



if __name__ == "__main__":
    game()