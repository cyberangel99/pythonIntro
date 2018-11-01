#Mary Green
#03/05/2018
#Unit 5
#LrgSml.py
#Designing a program with a loop that has the user enter a series of numbers

#the main function
def main():
    SENTINEL_VALUE= -99
#Ask user to input a number
    Input_Series= float(input('Enter a number:'))
    print(Input_Series)
#initializing the variables to the user input
    Smallest= Input_Series
    Largest=Input_Series
#while loop continues until the user enters -99
    while Input_Series != SENTINEL_VALUE:
#asks user to input another number
        Input_Series= float(input('Enter another number:'))
        print(Input_Series)
#if statement that compares the largest and smallest number the user enters
        if Input_Series < Smallest:
            Smallest= Input_Series
        print(Smallest)
        if Input_Series > Largest:
            Largest= Input_Series
#calls the function that displays the largest number and the smallest number
        LargeAndSmall(Smallest, Largest)



        
def LargeAndSmall(S,L):
    print('This is your smallest number', S)
    print('This is your largest number', L)


main()

#Input: 13, 44, 34, 28
#Output: Smallest 13, Largest 44



