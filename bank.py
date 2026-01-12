def showBalance(balance):
    print("****************************")
    print(f"YOUR BALANCE IS : {balance}")
    print("****************************")
    return

def withdraw(balance):
    print("****************************")
    print("ENTER AMOUNT : " , end="")
    amount = float(input())
    if amount < 0:
        print("ENTER VALID AMOUNT")
        return 0
    elif amount > balance:
        print("INSUFFIECIENT BALANCE")
        return 0
    else:
        return amount

def deposit():
    print("****************************")
    print("ENTER AMOUNT : " , end="")
    amount = float(input())
    if amount < 0:
        print("ENTER VALID AMOUNT")
        return 0
    else:
        return amount


def main():

    active = True
    balance = 0
    while active:
        print("****************************")
        print("WELCOME TO BANK -")
        print("1 . DEPOSIT")
        print("2 . SHOW BALANCE")
        print("3 . WITHDRAW")
        print("4 . EXIT")

        choice = int(input())

        match  choice:
            case 1 :
                balance += deposit()
            case 2 :
                showBalance(balance)
            case 3 :
                balance -= withdraw(balance)
            case 4 :
                active = False

if __name__ == "__main__":
    main()