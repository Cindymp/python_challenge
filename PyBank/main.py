import csv
import os

budget_csv = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("AnalysisPyBank", "resultsPyBank.txt")

total_months = 0
month_of_change = []
net_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]
total_net = 0

with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)  

    for row in csvreader:
        total_months += 1

        total_net += int(row[1])

        if total_months > 1:
            net_change.append(int(row[1]) - previous_amount)
            month_of_change.append(row[0])

        if int(row[1]) > greatest_increase[1]:
            greatest_increase = [row[0], int(row[1])]
        if int(row[1]) < greatest_decrease[1]:
            greatest_decrease = [row[0], int(row[1])]

        previous_amount = int(row[1])

average_change = sum(net_change) / len(net_change)

analysis_result = (
    f"AnalysisPyBank\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(analysis_result)

with open(file_to_output, "w") as txt_file:
    txt_file.write(file_to_output)

