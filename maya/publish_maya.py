import os
from shutil import copyfile
import maya.cmds as cmds

# This script should be used to move an asset version from the edit to the publish folder
# It also backups the last publish and makes sure the naming conventions are ok

def main():
    naming = checkNamingConvention()
    
    # Setting up vars from the naming convention
    asset = naming[0]
    saveType = naming[1]
    currentDir = naming[2]
    publishDir = naming[3]
    
    # Save the edit version before copy
    save(asset, saveType, currentDir)
    
    # Publish making sure naming conventions are good
    publish(asset, saveType, currentDir, publishDir)
    
def checkNamingConvention():
    # Isolating FileName from Path
    filePath = cmds.file(query = True, sceneName = True)
    filePath = filePath.split("/")
    fileName = (filePath[len(filePath) - 1])
    
    # Split filename to identify the type of backup
    splitFileName = fileName.split("_")
    # removing the ".ma" from the filename
    Asset = (splitFileName[0])
    saveType = (splitFileName[1][:-3])
    
    # make directories
    currentDir = (filePath[:len(filePath) - 1])
    publishDir = (filePath[:len(filePath) - 2])
    
    # make paths from the directories vars
    currentDir = ("/".join(currentDir) + "/")
    publishDir = ("/".join(publishDir) + "/")
    
    return(Asset, saveType, currentDir, publishDir)
    
def save(asset, saveType, currentDir):
    cmds.file( save=True, type='mayaAscii' )
    extension = ".ma"
    pathToFile = (currentDir + asset + "_" + saveType + extension)
    print(pathToFile)
    removeStudentMsg(pathToFile)
    
def publish(asset, saveType, currentDir, publishDir):   
    print(asset, saveType)
    extension = ".ma"
    copyfrom = (currentDir + asset + "_" + saveType + extension)
    copyTo = (publishDir + asset + "_" + saveType + extension)
    print(copyfrom)
    print(copyTo)
    if str(saveType) == "LOOKDEV":
        copyfile(copyfrom, copyTo)
    else:
        print("Asset is not LOOKDEV type -- Naming convention should be AssetName_LOOKDEV.ma")
    return(copyTo)
        
def publishBackup():
    # Need to check if a publish version exists
    # If yes, check if a publishBackup folder exists - if not, create the folder
    # Backup the previous publish before making the save over the original publish
    
    
    
def removeStudentMsg(pathToFile):
    # Opening the file and storing the lines in a list
    f = open(pathToFile, "r")
    lines = f.readlines()
    f.close
    
    # checking if the 13th line is student version
    checkMessage = ("Checking the file :" + str(pathToFile))
    print(checkMessage)
    licenseMessage = 'fileInfo "license" "student";'
    subcurrent = 0
    for i in lines:
        if lines[subcurrent].startswith(licenseMessage):
            # Check the line
            print("StudentVersion removed")
            del lines[subcurrent] # Remove the line
            
                
        else:
            pass
            
            
        subcurrent += 1
    
    # Reopen the file to write without the student line
    f = open(pathToFile, "w")
    f.writelines(lines)
    f.close()

if __name__ == "__main__":
    main()