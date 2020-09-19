import os
import usr_tracking as ut
import getProject as gp
import backupchecker as bckpcheck

def main():
    # Read the usrList.json using the usr_tracking.py file
    userList = ut.main()
    print(userList)
    # Read the projectPath.json using the getProject.py file
    project = gp.main()
    print(project)
    # Call to the yet to be defined backup function usingg the backupchecker.py
    bckpcheck.main()
    


if __name__ == "__main__":
    main()