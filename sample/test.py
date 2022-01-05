with open("sample/english.txt", "r") as f:
    words = []
    for i in f:
        words.append(i)
    
    for i in range(len(words)):
        words[i] = words[i].split("\\")
    
    
print(words)