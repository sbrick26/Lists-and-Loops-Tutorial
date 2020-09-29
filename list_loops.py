songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[len(songs) - 1])

print(songs[1:3])

songs[0] = "Butterfly Effect"

print(songs)

songs.extend(["Neon", "Lemonade", "Dil Nadia"])
print(songs)

del songs[1]

print(songs)

animals = ["Fish", "Snake", "Turtle"]
animals.append("Bird")
print(animals[2])
del animals[0]

for animal in animals:
    print(animal)
    