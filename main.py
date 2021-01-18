import random
import sys 
list = ['dog', 'chocolatemilk', 'picknick', 'shoppingcart', 'computer', 'music', 'tea', 'sunrise', 'beach', 'baseball', 'fireball', 'party', 'goose', 'sad', 'shower', 'tears', 'fighting', 'naïve', 'daisy', 'flowers']

#print woord
doggo = random.choice(list)
print(str(doggo))

#Intro 
naam = input("wat is je naam")
print("hallo " + naam, "laten we galgje spelen :)")
woord = ' _ ' * len(str(doggo))
print(woord)
geraden_letters = []
fout_geraden_letters = []


tries = 10
while tries > 0:
    guess = input("raad een letter of woord")
    if len(guess) == 1 and guess.isalpha():
      if guess in geraden_letters:
        print("oeps die heb je al geprobeerd")
    elif len(guess) == 1 and guess.isalpha():
        if guess not in doggo:
          print("jammer die zit er niet in")
          tries -= 1
         print("je hebt nog", + tries, "pogingen")
         fout_geraden_letters.append(guess)
         geraden_letters.append(guess)
         print("fout geraden letters", + fout_geraden_letters)
    elif len(guess) == 1 and guess.isalpha():
      if guess

reactie = input("wil je nog een keer spelen?")
while true:
  if reactie == ja
    break
  elif reactie == nee
    sys.exit("jammer, doeidoei")
