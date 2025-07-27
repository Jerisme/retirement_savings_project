print("Welcome to the Retirement Savings Calculator!\n")

annual_contribution = float(input("Enter your annual contribution: "))
total_savings = 0

print("\nYear | Annual Savings | Interest (3%) | Total Savings")
print("-------------------------------------------------------")

for year in range(1, 31):
    interest = total_savings * 0.03
    total_savings += annual_contribution + interest
    print(f"{year:<4} | ${annual_contribution:<14,.2f} | ${interest:<13,.2f} | ${total_savings:,.2f}")
