import os
from shutil import copyfile
import maya.cmds as cmds

# The goal of this file is to overwrite the current save, backup the previous one in a backup folder specifying the type of backup
# The architecture should look like this:
# Example   :   save    /   Asset           /   Backups /   BackupType  / Bacupfile
# Project   /   save    /   Eva_lookdev.ma  /   Backups /   lookdev     / Eva_lookdev_####.ma


def main():
    # Initializing the name and checking folders to allow backup
    backupList = checkNamingConvention()
    
    # Passing arguments for the backup save system
    asset = backupList[0]
    saveType = backupList[1]
    backupPath = backupList[2]
    originalPath = backupList[3]
    
    # Making the actual backup
    makeBackup(asset, saveType, backupPath, originalPath)
    
    # Saving the currentFile
    save(asset, saveType, originalPath)

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
    
    # Check for backupfolder
    currentDir = (filePath[:len(filePath) - 1])
    backupDir = ("/".join(currentDir)) + "/Backups/"
    
    # Check if the backup folder exists
    if not os.path.exists(backupDir):
        os.makedirs(backupDir)
        print("Created Backup Directory")
    else:
        print("Backup Directory exists")
        
    # Check if the secondary layer of backup exists
    secondaryBackup = backupDir + saveType + "/"
    print(secondaryBackup)
    
    if not os.path.exists(secondaryBackup):
        os.makedirs(secondaryBackup)
        print("Created " + saveType + " Directory")
    else:
        print(saveType + " Directory exists")
    
    currentDir = "/".join(currentDir) + "/"  
    return(Asset, saveType, secondaryBackup, currentDir)
        
def makeBackup(asset, saveType, backupPath, originalPath):
    extension = ".ma"
    # Check if the current Backup Folder is empty
    if not (os.listdir(backupPath)):
        copyFrom = (originalPath + asset + "_" + saveType + extension)
        copyTo = (backupPath + asset + "_" + saveType + "." + "0000" + extension)
        copyfile(copyFrom, copyTo)
    else:
        # Identifying the last backup file
        backupList = (os.listdir(backupPath))
        lastBackup = backupList[len(backupList) - 1]
        # Splitting the file name to find the numbering of the last file
        nameNumbering = (lastBackup.split("."))
        nameNumbering = nameNumbering[1]
        currentVersion = (int(nameNumbering)) + 1
        currentVersion = (str(currentVersion).zfill(4))
        # Making the final paths for copy of the numbered backup
        copyFrom = (originalPath + asset + "_" + saveType + extension)
        copyTo = (backupPath + asset + "_" + saveType + "." + currentVersion + extension)
        copyfile(copyFrom, copyTo)
        
    removeStudentMsg(copyTo)
                
    
    
def save(asset, saveType, originalPath):
    # Save the file
    cmds.file( save=True, type='mayaAscii' )
    
    extension = ".ma"
    currentFilePath = originalPath + asset + "_" + saveType + extension 
    removeStudentMsg(currentFilePath)
    
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