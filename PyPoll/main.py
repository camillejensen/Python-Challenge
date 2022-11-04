import os
import csv
csvpath = os.path.join("/Users/camillejensen/Desktop/Python-Challenge/PyPoll/Resources/election_data.csv")

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

with open(csvpath,newline="", encoding="utf-8") as elections:
     csvreader = csv.reader(elections,delimiter=",")
     header = next(csvreader)

     for row in csvreader:
          total_votes +=1
          if row[2] == "Khan":
               khan_votes +=1
          elif row[2] == "Correy":
               correy_votes +=1
          elif row[2] == "Li":
               li_votes +=1
          elif row[2] == "O'Tooley":
               otooley_votes +=1
          if row[2] == "Charles Casper Stockham":
               stockham_votes +=1
          elif row[2] == "Diana DeGette":
               degette_votes +=1
          elif row[2] == "Raymon Anthony Doane":
               doane_votes +=1

candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [stockham_votes, degette_votes, doane_votes]
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) *100
li_percent = (li_votes/total_votes) *100
otooley_percent = (otooley_votes/total_votes) *100
stockham_percent = (stockham_votes/total_votes) *100
degette_percent = (degette_votes/total_votes) *100
doane_percent = (doane_votes/total_votes) *100

print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")
