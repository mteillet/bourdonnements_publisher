import os

# The goal of this script is to create a list containing the name and locations of each shots in the project folder

def main(project):
    shotsFolder = str(project[0]) + "\\05_shot\\"
    alldirs = (os.listdir(shotsFolder))
    
    listShots = []

    current = 0
    for i in alldirs:
        if (alldirs[current][:3]) == "seq":
            listShots.append(alldirs[current])
            
        current += 1

    return(listShots)

if __name__ == "__main__":
    main()