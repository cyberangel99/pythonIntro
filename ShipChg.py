#Mary Green
#2/26/2018
#Unit 4 assignment
#ShipChg.py
#A program that determines the shipping cost based on the package weight.

#User to enter the package weight
def main():
	Weight = 0;
	Weight = float(input('Enter package weight:'))
	print("This is the weight you entered:")
	print(Weight)
#calling the calculation and shipping statement 
	CalcAndDisplayShipping(Weight)

#calculation statment, calculates shipping prices	
def CalcAndDisplayShipping(wt):
#constant variables
        UNDER_TWO = 1.10
        TWO_TO_SIX = 2.20
        SIX_TO_TEN = 3.70
        OVER_TEN = 3.80

        Shipping = 0;
#determines the shipping cost based on the weight
        if wt > 10:
           Shipping = wt * OVER_TEN
        elif wt > 6:
           Shipping = wt * SIX_TO_TEN
        elif wt > 2:
           Shipping = wt * TWO_TO_SIX
        else: 
           Shipping = wt * UNDER_TWO
        print("Shipping charge: $", format(Shipping, '.2f'))
        
#calls the main function
main()

#This is the input: 8
#This should be the output: $29.60
