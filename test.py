    # Imports

import json

    # Connect funds DB


def clrscr():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def printline():
    print("#################################################################")
    
def small_line():
    i=1
    print('  ',end='')
    while(i<20):
        print('*',end='')
        i+=1

def big_line():
    i=1
    print('\t',end='')
    while(i<50):
        print('*',end='')
        i+=1
        

    # Login Function

def login_user():
    
    print('\n')
    small_line()
    print('\n\tUSER LOGIN')
    small_line()
    username = str(input("\n\nPlease enter your username : "))
    pw = str(input("Please enter your password : "))
    users = open('test.txt','r')
    _users = json.loads(users.read())
    users.close()
    if(_users[username] == pw):
        print("\n***You have logged in successfully***")
        return str(username)
    else:
        print("\n***Login Credentials didn't match***\n")
        input()
        login_user()
        return 0
    
def login_mod():
    print('\n')
    small_line()
    print("\n    MODERATOR LOGIN")
    small_line()
    mod_username = str(input("\n\nPlease enter your username : "))
    mod_pw = str(input("Pease enter your password: "))
    mod = open('Moderator.txt','r')
    _mod = json.loads(mod.read())
    mod.close()
    if(_mod[mod_username] == mod_pw):
        print("\nYou have logged in successfully\n")
        main_menu_mod()
        return str(mod_username)
    else:
        print("\n***Login Credentials didn't match***\n")
        #input()
        login_mod()
        return 0  
    
def login():
    print("\nSelect one of the following: ")
    print("\n\n [1] Login for Users \n\n [2] Login for Moderator: ")
    i=int(input("\n\t Enter your choice: "))
    if(i==1):
       login_user()
    
    elif(i==2):
       login_mod()
       
    else:
        print("\n\n\t****Error : Please enter a valid choice !!! ****\n")
        login()
        
    # Signup Function

def signup():
    print('\n')
    small_line()
    print('\n\tSIGNUP')
    small_line()
    username = str(input("\nPlease enter your username : "))
    pw1 = str(input("Please enter your password : "))
    pw2 = str(input("Please confirm your password : "))
    users = open('test.txt','r') 
    _users = json.loads(users.read())
    users.close()
    bal = open('funds.txt','r') 
    _bal = json.loads(bal.read())
    bal.close()
    if pw1 == pw2 and pw1!='' and pw1!='\n' and pw1!='\t' and username!='':
        if username not in _users:
            updated_users = open('test.txt','w')
            _users[str(username)] = pw1
            updated_users.write(json.dumps(_users))
            updated_users.close()
            updated_bal = open('funds.txt', 'w')
            _bal[str(username)] = 0
            updated_bal.write(json.dumps(_bal))
            updated_bal.close()
            input("\n\t***You have created an account succesfully!!*** \n\nPress any key to continue....")
            main_menu(username)
        else:
            print("\n\t***A user with that name already exists!!***")
            signup()
    else:
        print("\n\t***Passwords you entered didn't match, PLEASE TRY AGAIN***")
        input()
        signup()
        
        #Check balance for mod
def check_balance_mod():
    balmod = open('funds.txt','r')
    _balmod = json.loads(balmod.read())
    printline()
    print("\n\t\t Balance of User accounts: \n")
    printline()

    for x in _balmod:
        print("\n" + str(x) + " Has " +str(_balmod[x]) +" Rs. in their accoount. ")
        
    input("\n\tPress any key to continue....")
    main_menu_mod()

        #View all users ledger
def View_ledger_mod():
    print("\n")
    ledg_mod = open('ledg.txt','r')
    _ledg_mod = json.loads(ledg_mod.read())
    ledg_user = str(input("Enter username: "))
    for x in _ledg_mod:
        if ledg_user in x:
            print(x + "\n")

    input("This is the ledger of " + str(ledg_user)+ "\nPress any key to continue:...")        
    main_menu_mod()    


    
    # Main Menu User
def main_menu(user):
    print('\n\t\t'+chr(60),chr(60),chr(60)+' 1. Check Profile '+    chr(62),chr(62),chr(62))
    print('\n\t\t'+chr(60),chr(60),chr(60)+' 2. Transfer Funds '+   chr(62),chr(62),chr(62))
    print('\n\t\t'+chr(60),chr(60),chr(60)+' 3. Foreign Exchange '+ chr(62),chr(62),chr(62))
    print('\n\t\t'+chr(60),chr(60),chr(60)+' 4. Withdraw Amount '+  chr(62),chr(62),chr(62))
    print('\n\t\t'+chr(60),chr(60),chr(60)+' 5. Deposit Amount '+   chr(62),chr(62),chr(62))
    print('\n\t\t'+chr(60),chr(60),chr(60)+' 6. Exit from System '+ chr(62),chr(62),chr(62))
    choice=int(input("\n\tEnter your choice from 1 to 6: "))
    print('\n')

    if choice == 1 :
        check(user)
    elif choice == 2 :
        transfer(user)
    elif choice == 3 :
        foreign(user)
    elif choice == 4 :
        withdraw(user)
    elif choice == 5 :
        deposit(user)
    elif choice == 6 :
        print('\n\t\t***Exiting from System.....')
    else :
        print('\n\t***Please enter a valid choice !!**')
        main_menu(user)

    #Main Menu Mod
def main_menu_mod():
    big_line()
    print("\n\t\t\t Welcome Moderator")
    big_line()
 
    print("\n")
    printline()
    print("\t\t\t  MAIN MENU")
    printline()
    print("\n")
    print("< < <   1. Check Users' Balance   > > >")
    print("< < <   2. View Users' Ledger     > > >")
    print("< < <   3. Delete account         > > >")
    print("< < <   4. Update Forex Values    > > >")
    print("< < <   5. Return to Home Screen  > > >")
    choice3 = int(input("Enter your choice from 1 to 5:  "))

    if(choice3==1):
        big_line()  
        print("\n\t\t\tUSER BALANCE")
        big_line()
        print("\n")
        check_balance_mod()

    elif(choice3==2):
        big_line()
        print("\n\t\t\tUSER LEDGER")
        big_line()
        View_ledger_mod()

    elif(choice3==3):
        
        print("DELETE ACCOUNT")
        #call function

    elif(choice3==4):
        big_line()
        print("UPDATE FOREX VALUES")
        big_line()
        foreign_mod()  
        
    elif(choice3==5):
        main()

    # Check Profile 

def check(user):
    print('\n\t\t< < < 1. View Your Balance     > > >')
    print('\n\t\t< < < 2. View Ledger           > > >')
    print('\n\t\t< < < 3. Change Password       > > >')
    print('\n\t\t< < < 4. Return to Main Menu   > > >')
    choice1=int(input("\n\tEnter your choice from 1 to 4: "))
    if choice1==1:
        
        print('\n')
        big_line()
        print('\n\t\t\tVIEWING BALANCE')
        big_line()
        bal = open('funds.txt','r') 
        _bal = json.loads(bal.read())
        print('\n\n\t\tBalance of Your Account is ' + str(_bal[user]))
        input("\n\tPress any key to continue....")
        main_menu(user)
    elif choice1==2:
        
        print('\n')
        big_line()
        print('\n\t\t\tOPENING LEDGER')
        big_line()
        print("\n\n\tAll your transactions so far : \n")
        ledg = open('ledg.txt','r') 
        _ledg = json.loads(ledg.read())
        for l in _ledg:
            if user in l:
                print(l + "\n")
        input('\n\t This was the complete ledger of your Account \n\tPress any key to continue....')
        main_menu(user)
    elif choice1==3:
        
        print('\n')
        big_line()
        print('\n\t\t\tCHANGE PASSWORD')
        big_line()
        users = open('test.txt','r') 
        _users = json.loads(users.read())
        print('')
        curPass = str(input("\n\nEnter your current Password: "))
        if _users[user] == curPass:
            newPass = str(input("Please enter your new password : "))
            _users[user] = newPass
            updated_users = open('test.txt','w')
            updated_users.write(json.dumps(_users))
            print("\n\n***Your password has been changed successfully!***")
            main_menu(user)
        else: 
            print("\n\n***Password was incorrect!!***")
            check(user)
    elif choice1==4:
        print('\n\t***Returning to main menu***')
        main_menu(user)
    else:
        print('\n\t\t***Choose a correct option***')
        check()

    # Transfer Funds 

def transfer(user):
    bal = open('funds.txt','r') 
    _bal = json.loads(bal.read())
    i=1
    print('\n')
    big_line()
    print('\n\t\t\tTRANSFER FUNDS')
    i=1
    print('\t',end='')
    while(i<50):
        print('*',end='')
        i+=1
    person=str(input('\nEnter the name of the user to whom you want to transfer the funds: '))
    if person in _bal and person!=str(user):
        amount = int(input("\nPlease enter the amount you want to transfer : "))
        if int(_bal[user]) >= amount:
            _bal[user] = int(int(_bal[user]) - amount)
            _bal[person] = int(int(_bal[person]) + amount)
            updated_bal = open('funds.txt', 'w')
            updated_bal.write(json.dumps(_bal))
            updated_bal.close()
            ledg = open('ledg.txt','r') 
            _ledg = json.loads(ledg.read())
            _ledg.append(str(str(user) + " transfered "+ str(amount) + " to " + str(person)))
            updated_ledg = open('ledg.txt','w')
            updated_ledg.write(json.dumps(_ledg))
            updated_ledg.close()
            input("\n\t\tYou have successfully transfered " + str(amount) + " to " + person + "\n\tPress any key to continue...")
            main_menu(user)
        else: 
            print("\n\t***Please enter a valid amount***\n")
            main_menu(user)
    else:
        input("\n\t***Make sure you have entered a correct username !!\n\tPress any key to continue...")
        main_menu(user)

    # Withdraw 

def withdraw(user):
    i=1
    print('\n')
    print('\t',end='')
    while(i<50):
        print('*',end='')
        i+=1
    print('\n\t\t\tWITHDRAW AMOUNT')
    i=1
    print('\t',end='')
    while(i<50):
        print('*',end='')
        i+=1
    amt = int(input("\nPlease enter the amount you want to withdraw : "))
    bal = open('funds.txt','r') 
    _bal = json.loads(bal.read())
    if amt > 0 and amt <= _bal[user]:
        _bal[user] -= amt
        updated_bal = open('funds.txt', 'w')
        updated_bal.write(json.dumps(_bal))
        updated_bal.close()
        ledg = open('ledg.txt','r') 
        _ledg = json.loads(ledg.read())
        _ledg.append(str(user + " withdrawed " + str(amt)))
        updated_ledg = open('ledg.txt','w')
        updated_ledg.write(json.dumps(_ledg))
        updated_ledg.close()
        input("\n\t\tYou have successfully withdrawed " + str(amt) + "\n\tPress any key to continue...")
        main_menu(user)
    else:
        print("\n\t***Please enter a valid amount***\n")
        main_menu(user)

    # Deposit

def deposit(user):
    i=1
    print('\n')
    print('\t',end='')
    while(i<50):
        print('*',end='')
        i+=1
    print('\n\t\t\tDEPOSIT AMOUNT')
    i=1
    print('\t',end='')
    while(i<50):
        print('*',end='')
        i+=1
    amt = int(input("\nPlease enter the amount you want to deposit : "))
    bal = open('funds.txt','r') 
    _bal = json.loads(bal.read())
    if amt > 0:
        _bal[user] += amt
        updated_bal = open('funds.txt', 'w')
        updated_bal.write(json.dumps(_bal))
        updated_bal.close()
        ledg = open('ledg.txt','r') 
        _ledg = json.loads(ledg.read())
        _ledg.append(str(user + " deposited " + str(amt)))
        updated_ledg = open('ledg.txt','w')
        updated_ledg.write(json.dumps(_ledg))
        updated_ledg.close()
        input("\n\t\tYou have successfully deposited " + str(amt) + "\n\tPress any key to continue...")
        main_menu(user)
    else:
        print("\n***Please enter a valid amount***\n")
        main_menu(user)

    # Foreign Exchange

def foreign(user):
    print("\n")
    big_line()
    print('\n\t\t\tFOREIGN CURRENCY')
    big_line()
    print('\n< < < 1. US Dollar > > >')
    print('\n< < < 2. UK Pound > > >')
    print('\n< < < 3. EURO > > >')
    ch = int(input("\nPlease select the currency price you want to check : "))
    if ch==1:
        print("\n\tPrice of 1 US Dollar is 75 Rs.\n")
        main_menu(user)
    elif ch==2:
        print("\n\tPrice of 1 UK Pound is 102 Rs\n")
        main_menu(user)
    elif ch==3:
        print("\n\tPrice of 1 EURO is 82 Rs\n")
        main_menu(user)
    else:
        print("\n\tBack to the Main Menu\n")
        main_menu(user)

    # Main Function
def main():
    
    print('\n')
#    print('\t',end='')
    big_line()
    print("\n\n\t\tWelcome to Payment Wallet System\n")

#    print('\t',end='')
    big_line()
    print("\n\n\t\tPlease select a choice from below : \n\n [1] Login \n\n [2] Signup \n \n")
    i = input("\t Enter your choice : ")
    if int(i) == 1:
        user = login()
        if user!=0:
            print('\n')
            main_menu(user)
        else:
            main()

    elif int(i) == 2:
        # Signup Function
        signup()
    else:
        print("\n\n\t****Error : Please enter a valid choice !!! ****\n")
        main()

main()
    
