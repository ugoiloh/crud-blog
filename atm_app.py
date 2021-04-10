'''
Project Title: Mock ATM Project
Developer: Miracle Iloh
Project Background: The project minics a typical bank ATM machine with some additional features.
The user account creation feature was added to just add flare to the project.
Account creation feature can be added to the ATM machines
'''

from datetime import datetime
import random

#Create dummy users
users = {
    'user1': {'pass': 'pass1', 'bal': 500, 'complaints':[]},
    'user2': {'pass': 'pass2', 'bal': 1000, 'complaints':[]},
    'user3': {'pass': 'pass3', 'bal': 1500, 'complaints':[]}
}

print('Welcome to First Bank \n Putting you First')
print('Are you a new user?')
print('1. Yes')
print('2. No')

userStatus = int(input('Please, select an option: \n'))

#Create an account for a new user
if userStatus == 1:
    username = input('Create your username: \n')
    password = input('Create your password: \n')
    users[username] = {}
    users[username]['pass'] = password
    users[username]['bal'] = 0
    users[username]['complaints'] = []

    print('Your account has been successfully created')
    print('Please login')
else:
    print('Please login')
login = False
moreTransact = True
while login == False:
    username = input('Enter your username: \n')
    password = input('Enter your password: \n')

    if username in users.keys():
        if users[username]['pass'] == password:
            # datetime object containing current date and time
            now = datetime.now()
            # dd/mm/YY H:M:S
            loginTime = now.strftime("%d/%m/%Y %H:%M:%S")
            print(f'Welcome {username}! @ {loginTime}')
            login = True
            while moreTransact == True:
                print('These are the available options')
                print('1. Withdrawal')
                print('2. Cash Deposit')
                print('3. Complaints')
                selectedOption = int(input('Please, select an option: \n'))
                if selectedOption == 1:
                    #Make withdrawal
                    withdrawalAmt = int(input('How much would you like to withdraw? '))
                    if withdrawalAmt > users[username]['bal']:
                        print(f'Insufficient balance! Your current balance is {users[username]["bal"]}')
                    else:
                        users[username]['bal'] -= withdrawalAmt
                        print(f'Take your cash - {withdrawalAmt}')

                elif selectedOption == 2:
                    #Make deposit
                    depositAmt = int(input('How much would you like to deposit? '))
                    users[username]['bal'] += depositAmt
                    print(f'Your balance is {users[username]["bal"]}')

                elif selectedOption == 3:
                    userComplaint = input('What issue will you like to report? \n')
                    users[username]['complaints'].append(userComplaint)
                    print('Thank you for contacting us!')

                else:
                    print('You entered a wrong number, please try again')

                #check whether the user wants to do more transaction
                print('Do you want to do more transactions?')
                print('1. Yes')
                print('2. No')

                userMoreTransact = int(input('Please, select an option \n'))
                if userMoreTransact == 2:
                    moreTransact = False
                    print('Thank you for banking with us!')

        else:
            print('Incorrect password, please try again')
    else:
        print('Username not found, please, try again')
