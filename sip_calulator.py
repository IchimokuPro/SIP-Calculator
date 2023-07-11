import matplotlib.pyplot as plt

def sip_calculator(principal, monthly_investment, interest_rate, investment_period):
    total_investment = monthly_investment * investment_period
    interest_earned = (total_investment * interest_rate * investment_period) / 100
    maturity_amount = principal + total_investment + interest_earned
    return maturity_amount

def plot_investment_growth(principal, monthly_investment, interest_rate, investment_period):
    years = range(1, investment_period + 1)
    maturity_amounts = []

    for year in years:
        maturity_amount = sip_calculator(principal, monthly_investment, interest_rate, year)
        maturity_amounts.append(maturity_amount)

    plt.plot(years, maturity_amounts)
    plt.xlabel('Years')
    plt.ylabel('Maturity Amount')
    plt.title('Investment Growth Over Time')
    plt.show()

# Example usage:
principal = 10000
monthly_investment = 5000
interest_rate = 12
investment_period = 5

maturity_amount = sip_calculator(principal, monthly_investment, interest_rate, investment_period)
print("Maturity Amount:", maturity_amount)

plot_investment_growth(principal, monthly_investment, interest_rate, investment_period)
