import os

def main():
    pathUsr = path()
    Userlist = readUsrs(pathUsr)
    return(Userlist)

def path():
    path = "usrList.json"
    return(path)

# Reading the user list and getting read of the new lines characters
def readUsrs(path):
    file = open(path, "r")
    line = file.readlines()

    cleanNames = []
    current = 0
    for i in line:
        if "\n" in line[current]:
            tempVar = line[current][:-1]
            line[current] = tempVar
        else:
            pass
        current += 1

    return(line)

if __name__ == "__main__":
    main()