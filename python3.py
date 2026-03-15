num = input("Enter a number: ")

freq = {}

for a in num:
    if a in freq:
        freq[a] += 1
    else:
        freq[a] = 1

print("Digit frequencies:")
for a in freq:
    print(freq[a],'times',a)