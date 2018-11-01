
#Mary Gree
#02/19/2018
#Unit 3 Assignment
#KiloConv
#Designing a program that converts a distance to kilometers and then converts that distance into miles. 


def main():
    #asks the user for the distance in kilometers and display it.
    Kilometers = float(input('What is the distance in kilometers?'))
    print("This is the distance you entered:")
    print(Kilometers)
    #calling the convert function into the main function.
    convert_miles(Kilometers)

    



#This function converts the kilometers by passing the argument into the function and converts it into miles.
def convert_miles(Kilometers):
    miles = Kilometers * 0.6214
    print("This is the distance converted into miles:")
    print(miles)
    


main()

#Input: 88
#Output: 54.6832
