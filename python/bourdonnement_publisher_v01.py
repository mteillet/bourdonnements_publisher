import os
import usr_tracking as ut
import getProject as gp
import backupchecker as bckpcheck

def main():
    # Read the usrList.json using the usr_tracking.py file
    userList = ut.main()
    print(userList)
    bckpcheck.main()
    project = gp.main()
    print(project)
    


if __name__ == "__main__":
    main()