import os
#import maya.cmds as cmds
import usr_tracking as ut
import backupchecker as bckpcheck

def main():
    # Read the usrList.json using the usr_tracking.py file
    userList = ut.main()
    print(userList)
    bckpcheck.main()


if __name__ == "__main__":
    main()