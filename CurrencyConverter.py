import pandas as pd

# Creating ExchangeRates class
class ExchangeRates:
    def __init__(self, fileName):
        self.rate = pd.read_csv(fileName, usecols = ['USD/CAD']).iloc[-1].iloc[-1]

    def convert(self, fromCurrency, amount):
        self.__converted = 0

        if fromCurrency == "CAD":
            self.__converted = amount / self.rate
        elif fromCurrency == "USD":
            self.__converted = amount * self.rate
        
        return round(self.__converted, 2)

# Printing UI
print("\nCURRENCY CONVERTER (CAD & USD)\n" + 30 * "-")

fromCurrency = input("Which currency would you like to convert from? ").upper()
toCurrency = input("Which currency would you like to convert to? ").upper()
amount = input("How much would you like to convert? ($) ")

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

print("\n$" + amount + " " + fromCurrency + " converts to $" + converted + " " + toCurrency)