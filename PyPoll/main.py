import os
import csv
csvpath = os.path.join("/Users/camillejensen/Desktop/Python-Challenge/PyPoll/Resources/election_data.py")

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

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

candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]