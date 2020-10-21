# Pages 183 - 190

# Application provides a menu-driven tool for navigating a file system and gathering information on files.

# import both the os and os.path and variables
import os, os.path

# Global constants and variables
QUIT = "7"
COMMANDS = ("1", "2", "3", "4", "5", "6", "7")
MENU = """
1. List the current directory
2. Move up
3. Move down
4. Number of file in the directory
5. Size of the directory in bytes
6. Search for a filename
7. QUIT the program"""

# Definition of the main() function
def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        #  passes the user input to determine which fumnction to run
        runCommand(command)
        if command == QUIT:
            print("Have a nice day...")
            break

def acceptCommand():
    # Inputs and returns a legitimate command number.
    command = input("Please make a selection: ")
    if command in COMMANDS:
        return command
    else:
        print("Error: command not recognized")
        return acceptCommand

def runCommand(command):        
    if command == "1":
        listCurrentDir(os.getcwd())
    elif command == "2":
        moveUp()
    elif command == "3":
        moveDown(os.getcwd())
    elif command == "4":
        print("The total number of files is", countFiles(os.getcwd()))
    elif command == "5":
        print("The Total number of bytes in this directory is", countBytes(os.getcwd()))
    elif command == "6":
        target = input("Please enter the filename you are looking for: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("File not Found")
        else:
            for f in fileList:
                print(f)

def listCurrentDir(dirName):
    # Prints a list of the cwd's contents.
    lyst = os.listdir(dirName)
    for element in lyst:
        print(element)

def moveUp():
    # Moves up the parent directory
    os.chdir("..")
def moveDown(CurrentDir):
    # Moves down to the named subdirectory if it exists
    newDir = input("Please enter the directory name: ")
    if os.path.exists(CurrentDir + os.sep + newDir) and os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("Error: no such directory name!")

def countFiles(path):
    # Returns the number of files in the cws and all of its subdirectories
    count = 0
    lyst = os.listdir(path)
    # Once the list is created, loop through it checking each item one at a time
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    # For loop is now done
    return count

def countBytes(path):
    # Returns the number of bytes in the cwd and all its subdirectories
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
        return count

def findFiles(target, path):
    files = []
    lyst = os.listdir(path)
    # Once the list of contents is created, loop through them one element ata time to see if the target string is in the name
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(findFiles(target, os.getcwd))
            os.chdir("..")

# Global entry point to the main function for program execution
main()
