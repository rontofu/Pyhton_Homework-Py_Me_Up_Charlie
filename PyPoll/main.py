# Import
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(csv_header)
    #for row in csvreader:
        #print(row) to see dataset

    # Assign variables
    total_votes = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0


    # Read each row of the dataset and calacultate total votes
    for row in csvreader:
        total_votes = total_votes + 1
        

        # Caculate total votes for each candidate
        if str(row[2]) == str("Khan"):
            khan = khan + 1
        elif str(row[2]) == str("Correy"):
            correy = correy + 1
        elif str(row[2]) == str("Li"):
            li = li + 1
        elif str(row[2]) == str("O'Tooley"):
            otooley = otooley + 1
    
    # Check to see if everything is correct:
    #print(total_votes) to see total number of votes in the dataset
    #print(khan) to see total votes for Khan
    #print(correy) to see total votes for Correy
    #print(li) to see total votes for Li
    #print(otooley) to see total votes for O'Tooley


        # Convert total votes for each candidate into a %
        percent_khan = khan / total_votes
        percent_correy = correy / total_votes
        percent_li = li / total_votes
        percent_otooley = otooley / total_votes

    # Check to see if everything is correct:
    #print(format(percent_khan, ".3%"))
    #print(format(percent_correy, ".3%"))
    #print(format(percent_li, ".3%"))
    #print(format(percent_otooley, ".3%"))


        # Calculate the winner
        winner = max(khan, correy, li, otooley)

        if winner == khan:
            election_winner = "Khan"

        elif winner == correy:
            election_winner = "Correy"

        elif winner == li:
            election_winner = "Li"

        elif winner == otooley:
            election_winner = "Correy"

    # Check if election winner is correct:
    #print(election_winner)

    # Print Results
    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------")
    print(f"Kahn: {percent_khan:.3%} ({khan})")
    print(f"Correy: {percent_correy:.3%} ({correy})")
    print(f"Li: {percent_li:.3%} ({li})")
    print(f"O'Tooley: {percent_otooley:.3%} ({otooley})")
    print("-----------------------")
    print(f"Winner: {election_winner}")
    print("-----------------------")

    # Export results to Analysis folder and write in txt file
    output = os.path.join('Analysis', 'election_results.txt')

    with open(output, "w") as results:
        results.write("Election Results\n")
        results.write(f"-----------------------\n")           
        results.write(f"Total Votes: {total_votes}\n")
        results.write(f"-----------------------\n")
        results.write(f"Kahn: {percent_khan:.3%} ({khan})\n")
        results.write(f"Correy: {percent_correy:.3%} ({correy})\n")
        results.write(f"Li: {percent_li:.3%} ({li})\n")
        results.write(f"O'Tooley: {percent_otooley:.3%} ({otooley})\n")
        results.write("-----------------------\n")
        results.write(f"Winner: {election_winner}\n")
        results.write("-----------------------")