import random
print("Hello World!")

story = random.randint(1, 2)

(Name) = input("name: ")
(adjective1) = input("adjective:")
(noun1) = input("noun: ")
(adjective2) = input("another adjective: ")
(verb) = input("verb: ")
(Emotion) = input("emotion: ")
(location) = input("location:")
(PastTenseVerb) = input("Past tense verb: ")
(food) = input("food: ")
(Color) = input("color: ")

if story == 1:
	print(f" Dear Professor {(Name)}: I understand that I recived a D- on my paper about {(noun1)}s- However, I hope that I can remedy this with an explanation. My {(adjective1)} mother was {(verb)}ing nonstop at the time, and I was understandably {(adjective2)} about it. To make matters worse, I was away in {(location)} and had just {(PastTenseVerb)}. I hope you can feel {(Emotion)} for me at this time, as I humbly request an extension. PS: as for the {(food)} stain, that one's my bad. sorry. ")

if story == 2:
	print(f"LOST DOG: {(Name)}. My dog is {(Color)}, {(adjective1)}, and very, very {(adjective2)}. She likes to {(verb)} and eat {(food)}. The last time I saw her we were at {(location)}. Please help me find her! ")