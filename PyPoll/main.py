import os
import csv


# path to collect data from csv
electioncsv = os.path.join('C:/Users/EKR/Desktop/BootCampPy/python-challenge/PyPoll/election_data.csv')

print("Election Results")
print("-----------------------------------")

# read in csv file
with open(electioncsv, 'r') as csvfile:
    # split data
    csvreader = csv.reader(csvfile)
    header = next(csvreader)


    # 1. The total number of votes cast
    voteslist = []
    for row in csvreader:
        voteslist.append(row)

    totalvotes = len(voteslist)
    print(f"Total Votes: {totalvotes}")
    print("-----------------------------------")

    # 2. A complete list of candidates who received votes
    candidateslist = []
    for row in voteslist:
        candidateslist.append(row[2])
#    print(len(candidateslist))
    candidateset = set(candidateslist)
#    print(candidateset)

    # 4. The total number of votes each candidate won

    khanwins = candidateslist.count("Khan")
    liwins = candidateslist.count("Li")
    correywins = candidateslist.count("Correy")
    otooleywins = candidateslist.count("O'Tooley")
    totalnames = khanwins + liwins + correywins + otooleywins


    # 3. The percentage of votes each candidate won
    khanscore = round(khanwins / totalnames * 100, 3)
    liscore = round(liwins / totalnames * 100, 3)
    correyscore = round(correywins / totalnames * 100, 3)
    otooleyscore = round(otooleywins / totalnames * 100, 3)

    print(f"Khan: {khanscore}% ({khanwins})")
    print(f"Correy: {correyscore}% ({correywins})")
    print(f"Li: {liscore}% ({liwins})")
    print(f"O'Tooley: {otooleyscore}% ({otooleywins})")

    print("-----------------------------------")

    # 5. The winner of the election based on popular vote.
    canddict = {"Khan":khanscore, "Li":liscore, "Correy":correyscore, "O'Tooley":otooleyscore}
    def maxwinnerscore(d):
        # a) create a list of the dict's keys and values
        # b) return the key with the max value
        v=list(d.values())
        k=list(d.keys())
        return v.index(max(v))
    def maxwinner(d):
        # a) create a list of the dict's keys and values
        # b) return the key with the max value
        v=list(d.values())
        k=list(d.keys())
        return k[v.index(max(v))]
    print(f"Winner: {maxwinner(canddict)}")
    print("-----------------------------------")

### BRAINSTORMING NOTES ###

# STRATEGIES FOR #4
#def count_matching(condition, seq):
#    """Returns the amount of items in seq that return true from condition"""
#    return sum(1 for item in seq if condition(item))
#count_matching(meets_condition, my_list)

#    candidates = {}
#    winner = x
#    if candidates(c) > winner:
#        winner = candidates(c)
#    for c in candidateset:
#        candidates[c] = candidateslist.count()
