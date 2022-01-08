global i
i = 0

def add():
    global i
    i += 2
    return i

print(add())