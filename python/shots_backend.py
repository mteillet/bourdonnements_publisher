from getProject import main as projPath
from listShots import main as listShots

def main():
    projectPath = projPath()
    listShots(projectPath)
    
    
if __name__ == "__main__":
    main()