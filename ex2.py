import random

MAX_LINES=3
MAX_BET= 1000
MIN_BET= 1

ROWS=3
COLS=3

Symbol = {
   "A":2,
   "B":4,
   "C":6,
   "D":8
}

def get_slot_machine_spins(ROW,COl,Symbol):
   
   all_symbols=[]
   for Symbol,symbol_count in Symbol.items():
      for _ in range(symbol_count):
         all_symbols.append(Symbol)

         columns= []
         for COL in range(COLS):
              column= []  
              current_symbols=all_symbols[:]
              for ROW in range(ROWS):
                  value= random.choice(current_symbols)
                  current_symbols.remove(value)
                  column.append(value)

                  columns.append(column)

   return columns
   
def print_slot_machine(columns):
   for ROW in range(len(columns[0])):
       for i, column in enumerate(columns):
            if i != len(columns):
              print(column[ROW], end=" | ")
            else:
                print (column[ROW])
           
            print()

def deposit():
    while True:
        amount=input("Enter amount to deposit: $")
        if amount.isdigit():
           amount=int(amount)
           if amount>0:
               break
           else:
            print("enter amount must be greater than 0")
        else:
            print("Please enter a positive number")     
        return amount
    
deposit()
def get_numbers_of_lines():
    while True:
     lines = input("Enter Number of lines to bet on (1-"+ str(MAX_LINES)+")? ")
     if lines.isdigit():
        lines = int(lines)
        if 1 <= lines <= MAX_LINES:
           break
        else:
         print("enter amount must be greater than 0")
     else:
        print("Please enter a positive number")

    return lines
get_numbers_of_lines()

def get_bet():
       while True:
        amount=input("Enter amount to bet: $")
        if amount.isdigit():
           amount=int(amount)
           if MIN_BET<= amount <= MAX_BET:
               break
           else:
            print(F"enter amount must be between ${MIN_BET} -${MAX_BET} ")
        else:
            print("Please enter a positive number")     
        return amount
    
slots= get_slot_machine_spins(ROWS, COLS,Symbol)

print_slot_machine

def main():
    balance=deposit()
    lines = get_numbers_of_lines()
    while True:
       bet= get_bet()
       total_bet= bet*lines
    print(f"you are betting ${bet} on {lines} lines. total is equal to: ${total_bet}")
    print(balance,lines)
    main()