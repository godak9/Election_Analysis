# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. Given election result data you are tasked to perform analysis and provide code that deleivers the outputs below:

1. Calculate the total number of cotes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Get a complete list of counties invloved in the election.
7. Calculate the total number of votes cast in each county.
8. Calculate the percentage of votes each county cast.
9. Determine the county with the largest voter turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.7, Visual Studio Code, 1.68.1

## Challenge Summary
### Election Audit Result
The election audit shows that:
- There were 369,711 votes cast in the election.
    - This was accomplised by opening the csv file containing the election results and creating a "for" loop to cycle through each row and add 1 to the varible "total_votes" with every cycle. The "total_votes" variable was initialized to 0.
```
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_vote = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header
    header = next(file_reader)
    print(header)
    # For each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes = total_votes + 1
```
- Jefferson county provided 38,855 votes and 10.5% of the total vote.
- Denver county provided 306,055 votes and 82.8% of the total vote.
- Arapahoe county provided 24,801 votes and 6.7% of the total vote.
  - To get each country present in the election we need to set the varible "county_name" equal to the first row in the csv file then create an "if" statement to check that the county name does match any existing county in the county list and begin tracking the counties in the "counties" list. Then to begin tracking the county's vote count, initialize every counties vote count to 0, and wrtie a new line in line with the "if" statment that increases the each counties vote count by 1 every time the county's name appears in the rows of data.
```
 # 3: Extract the county name from each row.
 county_name = row[1]
 # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
 if county_name not in counties:
    # 4b: Add the existing county to the list of counties.
    counties.append(county_name)
    # 4c: Begin tracking the county's vote count.
    county_votes[county_name] = 0
 # 5: Add a vote to that county's vote count.
 county_votes[county_name] +=1
```
- The county with the highest amount of votes cast was Denver County
  - To output the county with the highest voter turnout we first need to write a "for" loop to get the county from the county dictionary "county_votes" created earlier and create a new variable "votes" to retreive the county vote count. Next a varible "vote_percentage" was created to contain the output of "votes"/"total_votes" for each county. Finally, a nested "if" statement was created that stipulated if "votes" were greater than "largest_vote" (a variable set to zero earlier in the code) then the "largest_county" would be equal to "county_name" of whatever county had the largest vote.
```
# 1: Create a county list and county votes dictionary.
counties = []
county_votes = {}
# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_vote = 0
6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes)/float(total_votes) * 100
        # 6d: Print the county results to the terminal.
        county_results=( "County Results\n"
            f"{county_name}: {vote_percentage: .1f}% ({votes:,})\n")
        print(county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes>largest_vote):
            largest_vote = votes 
            largest_county = county_name 
```
- The candidates involved were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
 
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
  - A similar code was used to find the candidate options and their votes.
 ```
 # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
```
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  - A similar code was used to find the winning candidate.
```
 # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
        winning_percentage = vote_percentage
```
### Election-Audit Summary 
This code could be used for other elections if a similar data set were provided. Having three header columns helped define what exactly the "for" loops created should be searching for when iterating through the rows. One way to maybe make the code run faster would be to put the lines were saved a re being saved in text files at the end of all the "for" loops.

For example: Line 76...txt_file.write(election_results), Line 88...txt_file.write(county_results), Line 100... txt_file.write(largest_county_summary), Line 111...txt_file,write(candidate_results) can all be removed and added to the very last line, Line 127...txt_file.write(winning_candidate_summary).
