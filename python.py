intro = input('What is your name?')
character = 0
word = 1
for i in intro:
   character = character + 1
   if(i == ' '):
       word = word + 1
print('Number of words in your name')
print(word)
print('Number of characters in your name')
print(character)