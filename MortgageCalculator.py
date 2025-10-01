# Creating MortgagePayment class
class MortgagePayment:
    # In: The quoted interest rate and amortization period in years
    # Out: None
    # Desc: Initializing the mortgage payment class with the quoted interest rate and amortization period in years
    def __init__(self, rate, years):
        #Storing the interest rate as a decimal and amortization period in years
        self.__rate = rate / 100
        self.__years = years

    # In: The type of repayment structure as an integer of how many repayments are made during the year
    # Out: The periodic repayment amount rounded to 2 decimal places
    # Desc: Takes the type of repayment structure and applies the rearranged PVA formula to calculate payment per period 
    def __calcPayment(self, type):
        # Calculating the periodic interest rate and creating the number of periods
        r = (1 + self.__rate / 2) ** (1 / (type / 2)) - 1
        n = type * self.__years

        # Calculating and returning payment per period rounded to 2 decimal places by rearranging PVA formula 
        return round(self.__amount / ((1 - (1 + r) ** (-n)) / r), 2)
    
    # In: Pricipal mortgage amount
    # Out: The periodic payments as a tuple
    # Desc: Calculates and returns all periodic payments
    def payments(self, amount):
        # Storing principal amount, creating list of repayment types, and creating empty list to store payments
        self.__amount = amount
        periodList = [12, 24, 26, 52]
        paymentList = []

        # Looping through repayment types list to calculate periodic repayments
        for value in periodList:
            #Calculating perioding repayments
            paymentList.append(self.__calcPayment(value))
        
        # Calculating the accelerated periodic repayments
        paymentList.append(round(paymentList[0] / 2, 2))
        paymentList.append(round(paymentList[0] / 4, 2))
        
        # Returning the payment list as a tuple
        return tuple(paymentList)

# Printing UI
print("\nMORTGAGE CALCULATOR\n" + 25 * "-")

# Asking and storing user data related to interest rate, amortization period, and principal amount
rate = float(input("Input the Quoted Rate (%): "))
years = float(input("Input the Amortization Period (Years): "))
amount = float(input("Input the Principal Amount ($): "))

# Intializing mortgage object, calculating payments and creating an empty string to store payments as strings
mortgage = MortgagePayment(rate, years)
allPayments = mortgage.payments(amount)
strPayments = []

# Looping through payments to store as strings and adjust for 2 decimal place rounding
for value in allPayments:
    # Adding payment to string list
    strPayments.append(str(value))

    # Checking if the rounded number has decimal places
    if "." in strPayments[-1]:
        # Checking if the rounded number is not rounded to 2 decimal places
        if strPayments[-1][-3] != ".":
            # Adding the second decimal place
            strPayments[-1] += "0"
    else:
        # Adding both decimal places
        strPayments[-1] += ".00"
    
# Printing all the payments
print("\nMORTGAGE PAYMENTS\n" + 25 * "-" +
    "\nMonthly Payment: $" + strPayments[0] +
    "\nSemi-Monthly Payment: $" + strPayments[1] + 
    "\nBi-Weekly Payment: $" + strPayments[2] + 
    "\nWeekly Payment: $" + strPayments[3] +
    "\nRapid Bi-Weekly Payment: $" + strPayments[4] +
    "\nRapid Weekly Payment: $" + strPayments[5])