#Mary Green
#04/07/2018
#Unit 8 Data Files
#FileAvg.py
#Creating a program that calculates the average of all the numbers stored on a file.


def main():
    #openng the file to read the integers
    number_file = open('numbers.dat', 'r')
    string_input = number_file.readline()
    #creating a variable to use as a loop counter
    index = 0
    #adding the numbers in the files
    total = 0
    #looping thru the data file
    while string_input:
          value = int(string_input)
          index = index + 1
          total = total + value
          string_input = number_file.readline()
    #calucating the average
    Average = total/index
    print("The average of the integers", format(Average, '.2f'))



#calling the main function
main()
