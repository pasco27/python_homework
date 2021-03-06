# I've been provided budget_data.csv for analysis. 
# Data contains two columns: Date and P/L.
# The following is a script analyzing the data. 


# import libraries needed
import os
import csv

f = open("pybank_output.txt", "a")

# print a header for table cleanliness 
print("-"*27, file = f)
print("Financial Analysis", file = f)
print("-"*27, file = f)


# import the csv file 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
# I used this block of code to print the csv, checking format.
 #   for row in csv_reader:
 #       print(row)
 # 
 # I see there are two columns, and that the first row is a header titles 'Date' & 'Profit / Loss'    
 # Knowing that the first row is a header and seeing that the column1 data is monthly,
 # the total number of months in the data:
  
    csv_header = next(csv_reader)  # skips header in the count.
    data = list(csv_reader)
    row_count = len(data) 
    print(f'Total Months : {row_count}', file = f)

# net P/L for the dataset is the summation of that column 

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)  # again skipping header for the calc
    total_pl = 0
    for row in csv_reader: 
        total_pl += float(row[1])
        formatted_total_pl = "{:,.2f}".format(total_pl) # I'm using the same formatting here as below but still floats to 1 decimal
    print(f'Total P/L : ${total_pl}', file = f)

# average month/month P/L over entire dataet 

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader) 
    previous_row = 0 
    for row in csv_reader:
        difference = float(row[1]) - previous_row
        previous_row = float(row[1])
        avg_difference = (difference/(row_count))
        formatted_avg_diff = "{:.2f}".format(avg_difference) 
    print(f'Average Change: ${formatted_avg_diff}', file = f)

# greatest increase and decrease in profits, with date and amount

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader) 
    great_increase_row = max(csv_reader, key = lambda row: int(row[1]))
    print(f'Greatest Increase in Profits: {great_increase_row}', file = f)  # Need to work on this more to get $ in front 
 
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    great_decrease_row = min(csv_reader, key = lambda row: int(row[1]))
    print(f'Greatest Decrease in Profits: {great_decrease_row}', file = f)
 
 #   max_pl, min_pl = [], [] ????
  #  for row in csv_reader:
   #     max_pl.append(float(row[1]))   # not quite LOL
    #    min_pl.append(float(row[1]))
    #print(f'Greatest Increase in Profits: ${max_pl}')
    #print(f'Greatest Decrease in Profits: ${min_pl}')


# exported a text file with results to Analysis folder! 
# I completed this task after the program was written by going back and adding the file = f argument 
# to the print statements. 






#######################

# I think there's a much better way to do to this. 
# Noted a good youtube on lists. 
# Wondering if I can create a list of both month and P/L values.
# Can then easy find the min / max of the P/L list
