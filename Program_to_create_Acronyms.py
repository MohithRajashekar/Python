#Program to create Acronyms

inp = str(input("Enter a Phrase: ")) #input from users
text = inp.split()   #splits the phrase into each character
a = " "              #initialised to store the acronym of the phrase
for i in text:
    a = a+str(i[0]).upper() #store index value of str[0] of every word after a split and turn it into an uppercase format 
print(a)
