# write a program called invest.py that tracks the growing amount of an investment over time.# The initial deposit for an investment is
#called the principal amount.Each year, the amount increases by a fixed percentage, called the annual rate of return.
# For example, a principal amount of $100.00 with an annual rate of return of 5 percent increases the first year by $5.00 for a new amount
# of $105.00. The second year, the increase is 5 percent of $105.00, or $5.25, bringing the total to $110.25.

def invest(amount,rate,years):
    for i in range(1, years + 1):
        total_amount= amount + (rate/100 * amount)
        print(f'Year {i}: {total_amount:,.2f}')
        amount=total_amount #We can remove this and instead use amount= amount + (rate/100 * amount) in line 8

amount=float(input("Enter a principal amount: "))
rate=float(input("Enter an annual rate of return: "))
years=int(input("Enter number of years: "))

invest(amount,rate,years)





