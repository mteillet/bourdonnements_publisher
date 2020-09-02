from getProject import main as projPath
from listShots import main as listShots

# Analyzes the shot folder and print out a list of the location of each shot

def main():
    projectPath = projPath()
    allShots = listShots(projectPath)

    current = 0
    for i in allShots:
        print (projectPath[0] + "\\05_shot\\" + allShots[current])
        current += 1


    #### WRITING TO THE JSON FILE
    path = "shotList.json"

    with open(path, 'w') as f:
        for item in allShots:
            f.write("%s\n" % item)

    
    
    
if __name__ == "__main__":
    main()