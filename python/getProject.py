import os

def main():
    pathUsr = path()
    projPath = readProj(pathUsr)
    return(projPath)

def path():
    path = "projectPath.json"
    return(path)

# Reading the user list and getting read of the new lines characters
def readProj(path):
    file = open(path, "r")
    line = file.readlines()

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