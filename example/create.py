file = "/Users/steph/Desktop/Biodata.txt"
with open(file, "r") as f:

    # To split lines and assign to a list
    # With <word>\<word>
    match = []
    for i in f:
        match.append(i)
    # Remove \n from the end of the line
    match = map(lambda s: s.strip(), match)

    # To split every element inside the list by \
    # Assign it to a list
    words = [i.split("\\") for i in match]


    # Change to dictionary
    card = {}
    for i in range(len(words)):
        card[words[i][0]] = words[i][1]

    print(card)
    
