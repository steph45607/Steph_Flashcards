x = open("notes.txt", 'r')

lines = x.readlines()

# access contents of file in a list type
lst = []
count = 0
for line in lines:
    count = count + 1
    lst.append(line)
    print(count,":", line,sep="", end="")

print(lst)