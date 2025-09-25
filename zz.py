s = "0123456789"
letters = list(s)
letters[0:3] = reversed(letters[0:3])
s = "".join(letters)
print(letters)