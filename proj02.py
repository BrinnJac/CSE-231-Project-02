'''CSE 231

The program should enable to the user to calculate his/her traveling expenses
using a rental car. The program has three options with different features that
fit the amount of miles the user has traveled. Furthermore, the user will experience
an error code if he/she inputs the wrong classification_code. '''

import math

def trip(Classification_code, days_amount, begin, end):
    if(end<begin):
        #Math for the total trip milage
        length = math.ceil(end + 10 - (begin % 10))/10
    else:
        length = (end-begin)/10
    
    #Math for the billing of the classification_code 'B'
    if Classification_code == 'B' or Classification_code == "b":
        billing = (0.25*length) + days_amount*40; float(billing)
        

    #Math for the billing of the classification_code 'W'
    if (Classification_code == 'W' or Classification_code == 'w'):
        #The math weeks is calculated, average miles to week, base charge
        weeks = math.ceil(days_amount/7); average_miles = length / weeks; charge = 190.00
        #if the user's average miles are below 900
        if average_miles <= 900:
            billing = 0; billing = charge *weeks
        #if the user's mileage is above 900 and below or equal to 1500
        elif average_miles > 900 and average_miles <= 1500:
            mcharge = 100.00; billing = (charge *weeks) + (mcharge*weeks)
        else:
            chargemw = 200.00; chargemm =0.25
            billing = (charge *weeks) + (chargemw * weeks) + (chargemm * (length - (1500 * weeks)))
        
    #Math for the billing of the classification_code 'D'
    if Classification_code == 'D' or Classification_code  == "d":
        average_miles = length/days_amount; billing = float (days_amount * 60.00)
        #If the users average miles is below 100
        if average_miles > 100:
            billing += ((average_miles-100)*(0.25))*days_amount

    #The summary of the customers trip and bill expenses
    print("\nCustomer summary:")
    print("\tclassification code:", Classification_code)

    if(Classification_code == 'B' or Classification_code == 'b' or Classification_code == 'D' or Classification_code == 'd'):
        print("\trental period (days):",days_amount)
    else:
        print("\trental period (days):",days_amount)

    print("\todometer reading at start:",begin)
    print("\todometer reading at end:  ",end)
    print("\tnumber of miles driven: ",length)
    print("\tamount due: $",billing)
    print()

def display():
    #The user options will be displayed here
    print("\nWelcome to car rentals. \n")
    print("At the prompts, please enter the following: ")
    print("\tCustomer's classification code (a character: BDW) ")
    print("\tNumber of days the vehicle was rented (int)")
    print("\tOdometer reading at the start of the rental period (int)")
    print("\tOdometer reading at the end of the rental period (int)\n")


#Fuction is used to display the user options and allows him/her to interact with the program
def user_control():
    #display(): Questions
    display()
    answer=input("Would you like to continue (Y/N)? ")
    # Beginning of the loop. 
    while(answer=='y' or answer=='Y'):
        Classification_code=input("\nCustomer code (BDW): ")
        #Condition check for a Classification_Code other than what is listed below
        while(Classification_code !='W' and Classification_code !='w' and Classification_code !='B' and Classification_code !='b' and Classification_code !='D' and Classification_code !='d'):
            print("\t*** Invalid customer code. Try again. ***")
            #Prompts the user to try again
            Classification_code=input("\nCustomer code (BDW): ")
        #Continue statement for when the condition above is met
        else:
            days_amount = int(input("\nNumber of days: "))
    
        #User inputs car info
        begin=int(input("Odometer reading at the start: "))
        end=int(input("Odometer reading at the end:   "))
        trip(Classification_code, days_amount, begin, end)
        answer=input("Would you like to continue (Y/N)? ")
    print("Thank you for your loyalty.")
user_control()
