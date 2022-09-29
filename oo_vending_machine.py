# Created by: Lauren Humpherys

# Vending machine class
class vendingMachine:
    # Declare fields
    commandHistory = []
    currentBalance = 0
    inventory = []

    # Print initial greeting
    def __init__(self):
        print('\nWelcome to the Super Vending Machine!')
        print("To see a list of possible commands, simply type 'help'")

    # Pass vending machine and user command
    def addToHistory(self, command):
        # Append command to history
        self.commandHistory.append(command)

    # Show machine balance
    def printBalance(self):
        print('\nCurrent Balance in Machine: ${:.2f}' .format(self.currentBalance))
        print('\n')

    # Print command history
    def printHistory(self):
        print('\n   Command History:')
        print('**********************')
        print(*self.commandHistory, sep='\n')

    # Print inventory of items with price and quantity in stock
    def printInventory(self):
        print("Item Name | Price | Quantity\n")
        if not self.inventory:
            print("(Empty)\n")
        else:
            for item in self.inventory:
                print(item.name + '   ' + str(item.price) + '   ' + str(item.quantity))
    
    # Add item to inventory, including cost and quantity
    def addItem(self, item):
        # Append item inventory
        self.inventory.append(item)

    # When item is bought, take in: name, # dollars, # quarters, # dimes, # nickels, # pennies
    def buyItem(self, name, dollars, quarters, dimes, nickels, pennies):
        # Running total for transaction
        moneyIn = dollars + quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        # Check if item exists
        for item in self.inventory:
            if name == item.name:
                if(item.quantity >= 1):
                    # Make sure enough money 
                    if(moneyIn >= item.price):
                        # Remove 1 of specified item from inventory
                        item.decrementQty()
                        # Add to balance
                        self.currentBalance = self.currentBalance + item.price
                        # Calculate and return change
                        moneyIn = moneyIn - item.price
                        print('\nHere is your item, thank you for doing business with us!')
                        print('Your change is: $' +str(moneyIn))
                        return
                    else:
                        # Output error if not enough money is given
                        print("\nYou do not have enough money for that item. Please take your change and try again.")
                        return
                else:
                    # Output error if item of interest sold, but out of stock
                    print("\nThat item is out of stock. Please pick another item.")  
                    return
        # Return error if item is not part of inventory
        print("\nI do not sell that item yet. Please pick another item.")

# Items class
class Item:
    name = ''
    price = -1
    quantity = -1

    # Take in attributes for each item
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Update total quantity when item is purchased
    def decrementQty(self):
        self.quantity = self.quantity - 1

# Prints list of possible commands
def help():
    print('\nHere are the possible commands:')
    print(" - 'balance': Shows the balance")
    print(" - 'history': Shows the history")
    print(" - 'inventory': Shows the inventory")
    print(" - 'add item <item name> <integer quantity> <dollar price>'")
    print(" - 'buy item <item name> <# dollars> <# quarters> <# dimes> <# nickels> <# pennies>'")
    print(" - 'help': Displays this menu of possible commands")
    print(" - 'exit': Exits the Super Vending Machine")

# Prints goodbye message before exiting program
def exit():
    print('\nThank you, have a wonderful day!\n')

# ______________ MAIN FUNCTION ______________
vm = vendingMachine()       # Java equivalent: myClass var = new myClass()

while True:

    print('\nPlease input a command: ')
    command = input()
    vm.addToHistory(command)

    # All cases of potential functions
    if command == "balance":
        vm.printBalance()
    elif command == "history":
        vm.printHistory()
    elif command == "inventory":
        vm.printInventory()
    elif command.startswith("add item"):
        name = command.split(' ')[2]
        price = command.split(' ')[3]
        quantity = command.split(' ')[4]
        
        item = Item(name, float(price), int(quantity))
        vm.addItem(item)
    elif command.startswith("buy item"):
        boughtItemName = command.split(' ')[2]
        numDollars = command.split(' ')[3]
        numQuarters = command.split(' ')[4]
        numDimes = command.split(' ')[5]
        numNickels = command.split(' ')[6]
        numPennies = command.split(' ')[7]

        vm.buyItem(boughtItemName, int(numDollars), int(numQuarters), int(numDimes), int(numNickels), int(numPennies))
    elif command == "help":
        help()
    elif command == "exit":
        exit()
        break
    else:
        print("I'm sorry, I don't know how to do that yet...")
        print("Please type 'help' if you need to see a list of possible commands.")

    print("\nWhat else can I help you with today?\nIf you are finished, type 'exit'")