from tkinter import *
root = Tk()
root.title('Mortgage Calculator')

def button_calculate():
    """Executes the calculation."""
    property = int(property_box.get()) # Total value of property
    term = int(term_box.get()) # Mortgage term in years
    deposit = int(deposit_box.get()) # Initial deposit
    interest = int(interest_box.get()) # Interest rate as a percentage
    n = term * 12 #Mortgage term in months.
    i = (interest / 100) / 12 #Monthly interest rate as a decimal.
    PV = property - deposit #Mortgage amount
    monthly = int(((PV * i) * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
    total_cost = int(monthly * term * 12)
    monthly_box.insert(0, (f'Monthly cost: £{monthly}'))
    total_cost_box.insert(0, (f'Total amount: £{total_cost}'))

# Define entry boxes
property_box = Entry(root, width=35, borderwidth=5)
term_box = Entry(root, width=35, borderwidth=5)
deposit_box = Entry(root, width=35, borderwidth=5)
interest_box = Entry(root, width=35, borderwidth=5)
monthly_box = Entry(root, width=40, borderwidth=5, justify='center')
total_cost_box = Entry(root, width=40, borderwidth=5, justify='center')

# Define labels
property_label = Label(root, text='Property value in £')
term_label = Label(root, text='Term length in years')
deposit_label = Label(root, text='Deposit amount')
interest_label = Label(root, text='Interest rate in %')


# Define buttons
but_calculate = Button(root, text='Calculate monthly payment', padx=91, pady=20, command=button_calculate)


# Layout of entry boxes
property_box.grid(row=0, column=1)
term_box.grid(row=1, column=1)
deposit_box.grid(row=2, column=1)
interest_box.grid(row=3, column=1)
monthly_box.grid(row=4, columnspan=2)
total_cost_box.grid(row=5, columnspan=2)


# Layout of labels
property_label.grid(row=0, column=0)
term_label.grid(row=1, column=0)
deposit_label.grid(row=2, column=0)
interest_label.grid(row=3, column=0)


# Layout of buttons
but_calculate.grid(row=6, columnspan=2)




root.mainloop()
