with open("example/english.txt", "r") as f:

    # To split lines and assign to a list
    # With <word> \t <word>
    match = []
    for i in f:
        match.append(i)
    print(match)

    # To split every element inside the list by \t
    # Assign it to a dictionary
    words = []
    for i in f:
        for i in match:
            i.split("\t")
            words.append(i)
    
    print(words)
    
