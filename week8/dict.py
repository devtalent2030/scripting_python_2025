# 0️⃣  The dictionary exactly as you wrote it
data = {
    "fact":   "Cats only use their meows to talk to humans, not each other. "
              "The only time they meow to communicate with other felines is "
              "when they are kittens to signal to their mother.",
    "length": 170
}

# 1️⃣  Show the whole lunchbox
print("WHOLE DICT  →", data)

# 2️⃣  Grab just the fact (open the 'fact' drawer)
print("ONLY FACT   →", data["fact"])

# 3️⃣  Grab just the length (open the 'length' drawer)
print("ONLY LENGTH →", data["length"])

# 4️⃣  Peek at every drawer label and what’s inside
for key, value in data.items():
    print(f"{key!r} contains → {value!r}")

# 5️⃣  Safe lookup (returns None instead of crashing if key missing)
print("Maybe author:", data.get("author"))
