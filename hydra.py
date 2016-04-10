# Name: Hydra
# Author: Richard Rose
# Date: May 2015
# Description: Transposes information for analysis


# Import pandas to get access to dataframe
import pandas as pd

print "---------------------------------------------"
print " _   _           _           "
print "| | | |         | |          "
print "| |_| |_   _  __| |_ __ __ _ "
print "|  _  | | | |/ _` | '__/ _` |"
print "| | | | |_| | (_| | | | (_| |"
print "\_| |_/\__, |\__,_|_|  \__,_|"
print "        __/ |                "
print "       |___/                 "
print
print "---------------------------------------------"

# Read the csv file
data_file = pd.read_csv('hydra.csv')

# Initialise the data
df = pd.DataFrame()

# Check that the data is initialised
#print df

# How many records to read
records = len(data_file)

# Get the number of columns
columns = len(data_file.columns)

# Ask the user where to start transposing columns (S)

# fill an array with numbers, zero based to array start (S-1)

# Loop for each column item to transpose 
# e.g. If 44 column dates found and 36 to transpose, the range would be (8,44)

for data_index in range(8, columns):

	# initialise the data frame per iteration
	new_data = pd.DataFrame()

	# select the data for the iteration - amend N to be the number of records
	# Print data_file will indicate the number of rows (N) and columns
	# range(start, end)
	# column numbers - [0,1,2,3]
	new_data = data_file.ix[range(0, records),[0,1,2,3,4,5,6,7]]

	# Apply the column date to the information ingested
	new_data['Date'] = data_file.columns.values[data_index]


	# Read the cost data for the current column
	cost_data = data_file.ix[range(0, records),[data_index]]
	# Assign the cost data to the column
	new_data['Cost'] = cost_data

	# Append the data for later storage
	df = df.append(new_data, ignore_index=True)

# Output the data
#print df

# Open file
out = open('hydra_out.csv','w')

# output the dataframe to the open csv file
df.to_csv(out)

# close the file
out.close()
