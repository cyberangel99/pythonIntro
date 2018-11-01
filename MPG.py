#Mary Green
#5/6/18
#Unit 11
#MPG.py
# A program that calculates a car's miles per gallon

import tkinter
from tkinter import messagebox

class MpgGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.label1 = tkinter.Label(self.top_frame, \
                                          text ='Enter the number or gallons of gas the car holds:')
        self.gas_entry = tkinter.Entry(self.top_frame, \
                                       width=10)
        self.label2 = tkinter.Label(self.top_frame, \
                                          text ='Enter the number of miles the car is driven on a full tank:')
        self.miles_entry = tkinter.Entry(self.top_frame, \
                                       width=10)
        



        self.label1.pack(side='left')
        self.gas_entry.pack(side='left')
        self.label2.pack(side='left')
        self.miles_entry.pack(side='left')
        

        self.calc_button = tkinter.Button(self.bottom_frame, \
                                          text='Calculate MPG', \
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')


        self.top_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()


    def convert(self):
        gas = float(self.gas_entry.get())
        miles = float(self.miles_entry.get())
        


        Mpg = miles/gas

        messagebox.showinfo('Results', \
                                 str(miles) + str(gas) + ' calculates to ' + str(Mpg) + ' miles per gallon.')


Mpg_conv = MpgGUI()
                                        






















        
