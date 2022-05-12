print("\n            ")
print("Hello, there! I have a fun story about a mischievous dog. I can't wait to share it.")
print("\nBefore the story begins I have a few questions I need you to answer. ")
print("\nAfter each answer, please press the Enter key ")
print("\n Press any key to continue..")
dogBreed = input("\nWhat breed is the mischievous dog?")
dogName = input("\n What is the dog's name?")
dogCity = input("\n What city are you currently in?")
foodChoices = input("\n What is your favorite food?")
favoriteNumber = input("\n What is your favorite number?")
print ("\nLets begin.")
print("\nOnce day there was a mischievous", dogBreed, "named", dogName + ".")
print("\n" + dogName, "was very curious and liked to be adventurous. Today,", dogName, "felt like switching his routine up.")
sneakIntoKitchen = input("\nShould " + str(dogName) + " sneak into the kitchen to look for something tasty? Type yes or no: ")
if sneakIntoKitchen == "yes":
    print("\n" + dogName, "quitely sneaks into the kitchen to look for a tasty snack. He rips open", favoriteNumber, "bags of various snacks.")
    print("\n" + dogName, "is heard by his owners. They quickly run towards him to stop the chaos. Luckily," + dogName, "is fast! He bolts out the front door before he could be caught!")
else:
     print("\n" + dogName, "does not want to be risky and sneak into the kitchen.")
     print("\nInstead, he settles for a bland bowl of kibble by the front door. He proceeds to eat for", favoriteNumber, "minutes. Unforunately, the kibble was subpar.")
     print("\n" + dogName, "decides to go venture outside instead.")    
     
print("\n" + dogName, "is greeted by sunlight and Texas heat! He quickly notices that his owners have left the yard gate wide open.")
print("\n" + dogName, "is conflicted.")
      
sneakPastGate = input("\nShould he run out the gate and explore? Type yes or no: ")
if sneakPastGate == "yes":
    print("\n" + dogName, "has bolted out the gate to follow the sweet aroma of food!")
    print("\n" + dogName, "is greeted with varying aromas of", foodChoices,". He is filled with excitement until he stumbles across a pack of alley cats!")
    print("\nNervous, " + dogName, "barks", favoriteNumber, "times to warn the cats to stay away. He is successful and continues down the Texas alleyway.")
else:
    print("\n" + dogName, "decides to play in the backyard. Dogs that are", dogBreed, "have great tracking abilities.")
    print("\n" + dogName, "soon smells a squirrel and decides to follow that scent up a Texas dirt path.")
    print("\nHe is greeted by a larged apple tree.")

if sneakIntoKitchen == "yes" and sneakPastGate == "yes":
    print("\n" + dogName, "comes across a bakery after running from the mean alleycats.")
    print("\n" + dogName, "follows the aroma of french bread and begins to wolf down", favoriteNumber, "loaves of bread before being corned by the bakery owner.")
    print("\n" + dogName, "is identified by his collar. The bakery owner calls his owners to come pick him up.") 
    print("\n" + dogName, "is successfully returned home with a belly full of French bread and stern punishment from his owners")
elif sneakIntoKitchen == "yes" and sneakPastGate == "no":
    print("\n" + dogName, "looks for apples around the dirt path. He is greeted by a button nose.")
    print("\n" + dogName, "looks up and sees a friendly doe. They begin to follow the apples scent together")
    print("\n" + dogName, "spends all day looking for apples with his new doe friend!")
elif sneakIntoKitchen == "no" and sneakPastGate == "no":
    print("\n" + dogName, "has decided it is too hot to be chaotic today. He wants to stay near his water bowl!")
    print("\n" + dogName, "starts trotting down the yard until he a yellow spec catches his eye.")
    print("\n" + dogName, "finds his most prized possesion! His yellow squeaky banana. He lost this toy a few months ago and truly believed it was gone!")
    print("\n" + dogName, "begins running around the yard and runs into his deer friend! Togther they play and look for yummy apples to snack on")
elif sneakIntoKitchen == "no" and sneakPastGate == "yes":
    print("\n" + dogName, "sees alley cats and tries to scare them by showing his teeth!")
    print("\n" + dogName, "realizes this does not work for these cats! He quickly speeds down the alley.")
    print("\n" + dogName, "finds himself following the aroma of bread. He sees the bright red roof of a bakery and quickley bolts in.")
    print("\n" + dogName, "starts wolfing packs of muffins until he hears the footsteps of a bakery owner", str(dogName), "speeds out the door and runs all the way home! He makes it back inside the gate before his owners even noticed he was gone. What an adventure!")
















