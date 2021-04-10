'''
Project Title: Mock ATM Project
Developer: Miracle Iloh
Project Background: The project minics a typical bank ATM machine with some additional features.
The user account creation feature was added to just add flare to the project.
Account creation feature can be added to the ATM machines
'''

from datetime import datetime
import random
import time
from getpass import getpass
moreTransact = True

#Create dummy users
customerDatabase = {
    1234567890: {'pass': 'pass1', 'bal': 500, 'full_name': 'Jerry Luka','complaints':[], 'email': 'jerry@gmail.com'},
    1234568790: {'pass': 'pass2', 'bal': 1000, 'full_name': 'Terry Bola', 'complaints':[], 'email': 'terry@gmail.com'},
    1234567998: {'pass': 'pass3', 'bal': 1500, 'full_name': 'Bukky Demi', 'complaints':[], 'email': 'bukky@gmail.com'}
}

def account():
    print('*******Welcome to First Bank******* \n*******Putting you First*******')

    userStatus = int(input('Do you have an account with us? \n 1. Yes \n 2. No\n'))

    #Create an account for a new user
    if userStatus == 1:
        login()

    else:
        register()
#generate account number for new customers
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    login()

#Register new customers
def register():
    print('********** Please Register **********')
    accountNumber = generateAccountNumber()
    full_name = input('Enter your full name: \n')
    email = input('Enter your email: \n')
    
    # password1 = getpass()
    # password2 = getpass()
    password = input('Create your password: \n')
   
    customerDatabase[accountNumber] = {}
    customerDatabase[accountNumber]['full_name'] = full_name
    customerDatabase[accountNumber]['email'] = email
    customerDatabase[accountNumber]['pass'] = password
    customerDatabase[accountNumber]['bal'] = 0
    customerDatabase[accountNumber]['complaints'] = []
 
    print(f'Your account has been created successfully \nYour account number is {accountNumber}')

    login()

def login():
    print('********** Please Login **********')
    login = False
    
    while login == False:
        accNum = int(input('Enter your account number: \n'))
        password = input('Enter your password: \n')

        if accNum in customerDatabase.keys():
            if customerDatabase[accNum]['pass'] == password:
                # datetime object containing current date and time
                now = datetime.now()
                
                # dd/mm/YY H:M:S
                loginTime = now.strftime("%d/%m/%Y %H:%M:%S")
                print(f'Welcome {customerDatabase[accNum]["full_name"]}! @ {loginTime}')
                login = True
                return doTransaction(accNum)
            else:
                print('Incorrect password, please try again')
        else:
            print('Incorrect account number, please, try again')

def makewithdrawal(user):
    #Make withdrawal
    withdrawalAmt = input('How much would you like to withdraw? ')
    try:
        withdrawalAmt = int(withdrawalAmt)
    except Exception:
        print('Sorry, you must enter a valid number')
        makewithdrawal(user)
    else:
        if withdrawalAmt > customerDatabase[user]['bal']:
            print(f'Insufficient balance! Your current balance is \u20a6{customerDatabase[user]["bal"]}')
        else:
            customerDatabase[user]['bal'] -= withdrawalAmt
            print('Processing...') 
            #wait for 1 secs
            time.sleep(1) 
            print(f'Take your cash - \u20a6{withdrawalAmt}')

def makeDeposit(user):
    #Make deposit
    depositAmt = input('How much would you like to deposit? ')
    try:
        depositAmt = int(depositAmt)
    except Exception:
        print('Sorry, you must enter a valid number')
        makeDeposit(user)
    else:
        customerDatabase[user]['bal'] += depositAmt
        print('Processing...')
        time.sleep(1)
        print(f'Your currant balance is \u20a6{customerDatabase[user]["bal"]}')

def makeComplaint(user):
    userComplaint = input('What issue will you like to report? \n')
    customerDatabase[user]['complaints'].append(userComplaint)
    print('Thank you for contacting us!')

def checkBalance(user):
    print(f'Your currant balance is \u20a6{customerDatabase[user]["bal"]}')

def moreTransaction():
    userMoreTransact = input('Do you want to perform more transactions?  \n 1. Yes \n 2. No \n')

    try:
        userMoreTransact = int(userMoreTransact)
        
    except Exception:
        print(f'Sorry, you entered an incorrect value, {userMoreTransact}, try again')
        return moreTransaction()
    else:
        if userMoreTransact not in [1,2]:
            print('Sorry, you have made an invalid entry, try again')
            return moreTransaction()

        if userMoreTransact == 2:    
            print('Thank you for banking with us!')
            return False
        else: return True 

def doTransaction(user):
    moreTransact = True
    while moreTransact == True:

        selectedOption = input('Which transaction would you like to perform?\n 1. Withdrawal\n 2. Deposit\n 3. Complaints \n 4. Balance\n 5. Logout\n')
        try:
            selectedOption = int(selectedOption)
            
        except Exception:
            print(f'Sorry, you entered an incorrect value, {selectedOption}, try again')
            return doTransaction(user)
        else: 
            if selectedOption not in [1, 2, 3, 4, 5]:
                print('Sorry, you have made an invalid entry, try again')
                return doTransaction(user)
                
            if selectedOption == 1:
                makewithdrawal(user)

            elif selectedOption == 2:
                makeDeposit(user)

            elif selectedOption == 3:
                makeComplaint(user)

            elif selectedOption == 4:
                checkBalance(user)

            else: logout()

            moreTransact = moreTransaction()
        

account()
        
