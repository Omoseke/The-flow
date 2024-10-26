##This program defines a string and counts how many vowels are present in that string. It then displays the count of vowels.


# 
vowels = "aeiouAEIOU"

word_or_sentence = input("Enter a word or a sentence:")

counting_vowel = 0

for a in word_or_sentence:
    if a in vowels:
        counting_vowel +=1


print("The number of vowel is " , counting_vowel);




##This program has a function that takes a list of numbers and calculates their sum, providing the total sum as output to the user.

numbers = [2,5,6,9,2,5,2,7,3,4,7,4,4]

def sumfunc():
    total = 0
    for a in numbers:
        total += a
    print(total)   

sumfunc()
