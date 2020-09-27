songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[1:3])

songs[2] = "Wayward Daughter"

print(songs)

songs.extend(["Sunrise", "In the Dragon's Wake", "Return to Oblivion"])

print(songs)

del songs[0]

animals = ["Pig", "Snake", "Cat"]

animals.append("Boar")

print(animals[2])

del animals[0]

for animal in animals:
  print(animal)