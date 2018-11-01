#Mary Green
#03/30/2018
#Unit 7
#ValidAcct.py
#A program that asks the user to enter a number for a charge account.

def main():
      #creating an array declaration of valid account numbers
      accounts = [5658845, 8080152, 1005231, 4520125, 4562555, 6545231,
                  7895122, 5552012, 3852085, 8777541, 5050552, 7576651,
                  8451277, 7825877, 7881200, 1302850, 1250255, 4581002]
      #get user input for the charge account number
      ChargeNumber=int(input('Enter the charge account number:'))
      #get the length of the accounts numbers.
      TotalNums=len(accounts)
      #calling the validation function
      if isValidAccount(accounts, ChargeNumber, TotalNums):
         print('Your charge account number is valid.')
      else:
        print('Invalid, Enter a Valid charge account number.')

      #function that validates the charge account number
def isValidAccount(a, C, T):
  #creating a Boolean to act as a flag.
  found = False
  #creating a loop variable as a loop counter
  index = 0
  #Searches thru the accounts to find an account number equal to the user's input.
  while found ==False and index < T:
    if a[index] == C:
      found = True
    else:
      index = index +1
           
  return found
main()

#For a valid account number: Enter the charge account number:4581002
#Output: Your charge account number is Valid.
#For a invalid account number: Enter the charge account number: 67675454
#Output: Invalid, Enter a Valid charge account number.
