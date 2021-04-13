"""
A simple Budget app designed using classes
Developer: Miracle Iloh (ilohmiracle@yahoo.com)
The app can allow withdrawal, deposit, balance and transfer 
between categories(Food, Clothing, Entertainment)
"""

class Budget:

    def __init__(self, category, bal=0):
        self.category = category
        self.bal = bal

    def deposit(self, amt):
        try:
            amt = float(amt)
        except Exception:
            print('Please, enter a valid amount to deposit')

        else:
            self.bal += amt
            print(f'You deposited {amt} into {self.category} category')

    def withdraw(self, amt):
        try:
            amt = float(amt)

        except Exception:
            print('Please, enter a valid amount to withdraw')
        
        else:
            if self.bal > amt:
                self.bal -= amt
                print(f'You withdrew {amt} from {self.category} category')
            else:
                print('Your balance is insufficient for this transaction, please make deposit')

    def balance(self):
        print(f'You have {self.bal} left in the {self.category} category')

    def transfer(self, category, amt):
        try:
            amt = float(amt)

        except Exception:
            print('Please, enter a valid amount to transfer')

        else:
            if self.bal > amt:
                self.bal -= amt
                category.bal += amt
                print(f'You transfered {amt} from {self.category} to {category.category} category')
            else:
                print('Your balance is insufficient for this transaction, please make deposit')

# food = Budget('food', 20)
# cloth = Budget('cloth', 30)
# food.withdraw('q')


