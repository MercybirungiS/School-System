# madlibs game 
# name =input("Enter name:")
# hobby=input("Enter a hobby:")
# desert=input("Enter your favorite desert:")

# print ("My name is  " + name)
# print("I love "+hobby)
# print("I love "+desert)

word = str(input("Please Enter The Word:"))
wordlist=[]
j=1
for i in range(len(word)):
wordlist.insert(i,word[i:j])
j=j+1
print("Character Count: " + str(len(word) - wordlist.count(" ")))
print("Word Count: " + str(wordlist.count(" ")+1))