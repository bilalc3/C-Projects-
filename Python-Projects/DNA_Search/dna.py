from sys import argv, exit
import csv

if len(argv) != 3:
    print("Error: First command line argument is database name as csv")
    print("Second command line argyment is sequence as txt")
    exit (1)

csvfilename = argv[1]
txtfilename = argv[2]

#opening first file which is a csv file
with open (f'{argv[1]}' , mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print (f"columns names are {','.join(row)}")
            line_count +=1
        print (f"\t {row['name']} has {row['AGATC']} AGATC, {row['AATG']} AATG and {row['TATC']} TATC")
        line_count +=1
    print (f"Processed {line_count} lines")
print(row) #checking what is in there


#opening up the txt file for sequence
txt = open(f"{argv[2]}", "r")
if txt.mode  == 'r':
    linetxt = txt.read()
    print(linetxt)

if csvfilename == "databases/small.csv":
    dnalist = ["AAGT", "AATG", "TATC"]
    print (dnalist)
    numdna = 3
elif csvfilename== "databases/large.csv":
    dnalist = ["AAGT", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
    print (dnalist)
    numdna = 8

seqtype = linetxt
print (seqtype[2])
x =0
maxlist = []
for x in (len(dnalist)):
#SETTING VARIABLES
    position = 0
    preposition = 0
    counter  = 0
    maxcounter = 0
    while position < len(seqtype):
        position = seqtype.find(dnalist[x], position)
        #if not found
        if position == -1:
            counter = 0
            break
        # if the first set of char is the dna
        elif (position != -1) and (preposition == 0):
            counter +=1
            maxcounter = counter
            preposition = position
        #adding on if cosecutive
        elif (position != -1) and ((position - len(dnalist[x]))==preposition):
            counter +=1
            if maxcounter <counter:
                maxcounter = counter
            preposition = position
        #first dna but not the first char in the seq
        elif (position != 0) and ((position-len(dnalist[x]))!= preposition):
            counter  +=1
            if maxcounter < counter:
                maxcounter = counter
            preposition  = position
        position += 1
    maxlist.append(maxcounter)


for row in csv_reader:
    linecount = 0
    if linecount == 0:
        linecount += 0
    else:
        for x in numdna:
            if x == 0:
                x+=1
            elif row[x] == maxcounter [x]:



