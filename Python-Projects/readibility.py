from cs50 import get_string
from sys import exit

text = get_string("Text:")
letters=0
words=1
sentences=0
for char in range(len(text)):
    x = text[char]
    if text[char].isalpha() == True:
        letters +=1
    elif text[char].isspace()==True:
        words+=1
    elif text [char]=="." or text [char]=="?" or text[char]=="!":
        sentences+=1


L = (letters/words)*100
S = (sentences/words)*100
gradelevel = 0.0588 * L - 0.296 * S - 15.8

if gradelevel<0:
    print("Before Grade 1")
    exit(1)
elif gradelevel>16:
    print("Grade 16+")
    exit (1)
else:
    print(f"Grade:{round(gradelevel)}")

