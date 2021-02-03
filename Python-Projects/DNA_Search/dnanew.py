from sys import argv, exit
from csv import reader, DictReader

if len(argv) != 3:
    print("Error: First command line argument is database name as csv")
    print("Second command line argyment is sequence as txt")
    exit (1)

with open(argv[2]) as dnafile:
    dnareader = reader(dnafile)
    for row in dnareader:
        dnalist = row

dna = dnalist[0]
print (dna)
sequences ={}

with open(argv[1]) as peoplefile:
    people = reader(peoplefile)
    for row in people:
        dnaSequences = row
        dnaSequences.pop(0)
        print (dnaSequences)
        break
for item in dnaSequences:
    sequences[item] = 1
maxdna = []
for key in sequences:
    l = len(key)
    counter  =0
    maxcounter = 0
    for i in range(len(dna)):
        if counter >0:
            counter-=1
            continue
        if dna[i:i+l] == key:
            while dna[i-l:i] == dna[i:i+l]:
                counter +=1
                i+=l
            if counter >maxcounter:
                maxcounter = counter
    sequences[key]+= maxcounter

print (sequences)
