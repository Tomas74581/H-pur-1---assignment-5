#Fer í for lykkju sem fer n sinnum yfir 
#Gildið verður 1... 2...
#Síðan er summan af 1 og 2 lögð saman
#Eftir það er summan af 2 seinustu tölum lögð saman (3 og 2) en byrjar að bætast við +1
#+1 hækkar síðan alltaf um 1 (+2... +3...) ásamt því að summa tvær seinustu tölurnar
#Forritið skrifar síðan út rununa með kommu á milli frá 1-n.

n = int(input("Enter the length of the sequence: ")) # Do not change this line

first = 1
second = 0
third = 0
sequence = 0
for i in range(n):
    sequence = first + second + third
    third = second
    second = first
    first = sequence
    if sequence == 2:
        third = 0
    print(sequence)
