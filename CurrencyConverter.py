# QUESTION 2: Currency Converter

# Importing pandas
import pandas as pd

# Creating ExchangeRates class
class ExchangeRates:
    # In: Path to exchange rate file
    # Out: None
    # Desc: Stores the most recent exchange rate for USD/CAD
    def __init__(self, filePath):
        self.rate = pd.read_csv(filePath, usecols = ['USD/CAD']).iloc[-1].iloc[-1]

    # In: Currency to exchange from and how much to exchange
    # Out: Converted amount, rounded to 2 decimal places
    # Desc: Converts the amount from the currency given to the opposite currency
    def convert(self, fromCurrency, amount):
        # Initializing converted amount variable
        self.__converted = 0

        # Checking which currency the user wants to exchange from
        if fromCurrency == "CAD":
            # Converting from CAD to USD
            self.__converted = amount / self.rate
        elif fromCurrency == "USD":
            # Converting from USD to CAD
            self.__converted = amount * self.rate
        
        return round(self.__converted, 2)

# Printing UI
print("\nCURRENCY CONVERTER (CAD & USD)\n" + 30 * "-")

# Asking and storing user input for currencies and amount to exchange
fromCurrency = input("Which currency would you like to convert from? ").upper()
toCurrency = input("Which currency would you like to convert to? ").upper()
amount = input("How much would you like to convert? ($) ")

# Creating the exchange object and storing the exchanged amount
c = ExchangeRates('C:\\Users\\humza\\Downloads\\BankOfCanadaExchangeRates.csv')
converted = str(c.convert(fromCurrency, float(amount)))

# Checking if the rounded number has decimal places
if "." in converted:
    # Checking if the rounded number is not rounded to 2 decimal places
    if converted[-3] != ".":
        # Adding the second decimal place
        converted += "0"
else:
    # Adding both decimal places
    converted += ".00"

# Returing the users original amount and currency as well as converted amount and currency
print("\n$" + amount + " " + fromCurrency + " converts to $" + converted + " " + toCurrency)