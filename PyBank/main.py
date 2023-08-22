import pandas as pd

#import the buget data
file_path = "budget_data.csv"
data = pd.read_csv(file_path)

# The total number of months included in the dataset
total_months = len(data)

#The net total amount of "Profit/Losses" over the entire period

net_total = data["Profit/Losses"].sum()

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
data["Change"] = data["Profit/Losses"].diff()
average_change = data["Change"].mean()

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = data[data["Change"] == data["Change"].max()]

#The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = data[data["Change"] == data["Change"].min()]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total:.0f}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date'].values[0]} (${greatest_increase['Change'].values[0]:.0f})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date'].values[0]} (${greatest_decrease['Change'].values[0]:.0f})")

# Export Results to Text File
output_path = "financial_analysis.txt"
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total:.2f}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase['Date'].values[0]} (${greatest_increase['Change'].values[0]:.2f})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['Date'].values[0]} (${greatest_decrease['Change'].values[0]:.2f})\n")

print(f"Results have been printed to the terminal and saved to '{output_path}'.")
