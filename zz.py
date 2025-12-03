def ArrayChallenge(strArr):
    elements = [(len(word), word) for word in strArr]
    elements.sort(key=lambda x: (-x[0]))
    print(elements)
    return elements[2][1]

print(ArrayChallenge(["hello", "world", "before", "all"]))  # Output: "world"
print(ArrayChallenge(["hello", "world", "after", "all"]))    # Output: "after"