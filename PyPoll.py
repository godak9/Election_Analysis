PyPoll.py
#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each condiate won
#5. The winner of the election based on popular vote.
# Import the datetime class from the datetime module.
import datetime

# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Import the datetime class from the datetime module.
import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

#Assign a variable 
import csv
dir(csv)
file_to_load = open("election_results.csv", "r") 
#Open a direct path to the file and read the results
file_to_load= "Resources3/election_results.csv"
election_data= open(file_to_load, 'r')
print(election_data)

#Open the election results and read the file
with open(file_to_load) as election_data:
        print (election_data)


#Indirect path to the file. Add out dependencies 
import csv 
import os
dir(os)
#Assign a variable to load a file path
file_to_load = os.path.join("Resources3", "election_results.csv")
#Assign a variable to save the file to a path 
file_to_save=os.path.join("analysis", "election_analysis.txt")
#Open the election results and the read file
with open(file_to_load) as election_data:
        #Read the file object with the reader function 
        file_reader=csv.reader(election_data)
         #Read and print the header row, the first row
        headers=next(file_reader)
        print(headers)


#Using the open() function with the "w" mode will write data to the file
open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:
        txt_file.write("Arapahoe\nDenver\nJefferson")





      
       







     
