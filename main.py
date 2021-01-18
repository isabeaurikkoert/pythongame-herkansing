import random
import sys 
import time
list = ['dog', 'chocolatemilk', 'picknick', 'shoppingcart', 'computer', 'music', 'tea', 'sunrise', 'beach', 'baseball', 'fireball', 'party', 'goose', 'sad', 'shower', 'tears', 'fighting', 'naïve', 'daisy', 'flowers','noodles', 'schilderij', 'wandelen', 'knuffelen', 'verband', 'lockdown', 'kabinet', 'honger', 'biologie', 'scheikunde', 'toetsweek', 'leren', 'marathon', 'museum', 'voorwerp', 'attribuut', 'portretfoto', 'fotografie', 'husky', 'telefoon', 'piano', 'gitaar', 'zingen', 'netflix', 'videoland', 'koolstofmonooxide', 'giftig', 'dood', 'leven', 'god', 'hel', 'lampjes', 'vakantie', 'snowboarden', 'sneeuw', 'stoel', 'plant', 'kleiien', 'bakje', 'verven', 'kikker', 'cadeautje', 'verjaardag', 'rijbewijs', 'klok', 'tijd', 'openhaard', 'vuur', 'gevaar', 'warmte', 'gezelligheid']

#print woord
doggo = random.choice(list)
print(str(doggo))
temp = " _ " * len(str(doggo))
#Intro 
naam = input("wat is je naam")
print("hallo " + naam, "laten we galgje spelen :)")
woord = ' _ ' * len(str(doggo))
time.sleep(0.5)
print(woord)
geraden_letters = []
fout_geraden_letters = []

tries = 10
while tries > 0:
  guess = input("raad een letter")
  if len(guess) == 1 and guess.isalpha():
    if guess in geraden_letters:
      print("oeps die heb je al geprobeerd")
    elif guess not in doggo:
      print("jammer die zit er niet in")
      tries -= 1
      time.sleep(0.5)
      print("je hebt nog", + tries, "pogingen")
      fout_geraden_letters.append(guess)
      geraden_letters.append(guess)
      time.sleep(0.5)
      print("fout geraden letters:")
      print(sorted(fout_geraden_letters))
    else:
      print("goed geraden!")
      geraden_letters.append(guess)
      for i in range(0, len(str(doggo))):
          if guess == doggo[i]:
            temp = temp[:i] + guess + temp[i+1:]
            print(temp)
            time.sleep(0.5)
            print("je hebt nog", + tries, "pogingen")
            time.sleep(0.5)
            print('fout geraden letters:')
            print(sorted(fout_geraden_letters))
  if len(guess) != 1:
    print("je kan maar één letter per beurt proberen;)")
    tries -= 1
    time.sleep(0.5)
    print("je hebt nog", + tries, "pogingen")
    time.sleep(0.5)
    print('fout geraden letters:')
    print(sorted(fout_geraden_letters))
    break 
if tries == 0:
  print("jammer je beurten zijn om het woord was " + doggo, "volgende keer beter;)")

   


