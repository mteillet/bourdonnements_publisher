import os
#import maya.cmds as cmds
import usr_tracking as ut

def main():
    # Read the usrList.json using the usr_tracking.py file
    userList = ut.main()
    print(userList)


if __name__ == "__main__":
    main()