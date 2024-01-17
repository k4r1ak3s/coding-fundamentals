
vowels = ["a", "e", "i", "o", "u"]
count = 0
word_check = str(input("Input a word to check: "))

for i in range(len(word_check)):
    if word_check[i] in vowels:
        count += 1
        
print("Number of vowels in the given string is: ", count)
