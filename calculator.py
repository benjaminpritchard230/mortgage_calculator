property = int(input('Enter the total value of the property:\n')) #Total price of property
term = int(input('Enter the mortgage term in years:\n')) #Term in years
deposit = int(input('How much is your deposit?:\n')) #Deposit paid
interest = int(input('What is the offered interest rate?:\n')) #Annual interest rate as a percentage


n = term * 12 #Mortgage term in months.
i = (interest / 100) / 12 #Monthly interest rate as a decimal.
PV = property - deposit #Mortgage amount

monthly = ((PV * i) * ((1 + i) ** n)) / (((1 + i) ** n) - 1)
monthly = int(monthly)
print(f'A property worth £{property} bought with a {term} year mortgage and a deposit of £{deposit} would cost £{monthly} per month.')